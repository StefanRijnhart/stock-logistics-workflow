# Copyright 2020 Iryna Vyshnevska Camptocamp
# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare

CONTEXT_KEY_ACTIONS_CREATE_RETURNS_ALL = (
    "stock_picking_return_lot.action_create_returns_all"
)


class ReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    lots_visible = fields.Boolean(compute="_compute_lots_visible")

    @api.depends("product_return_moves.product_id.tracking")
    def _compute_lots_visible(self):
        for wiz in self:
            wiz.lots_visible = any(
                tracking != "none"
                for tracking in wiz.product_return_moves.product_id.mapped("tracking")
            )

    def _get_qty_by_lot(self, move):
        """Get all quantities that were shipped out, per lot"""
        qties = defaultdict(float)
        for sml in move.move_line_ids:
            qties[sml.lot_id] += sml.quantity
        for dest_move in move.move_dest_ids:
            if dest_move.origin_returned_move_id == move:
                for sml in dest_move.move_line_ids:
                    qties[sml.lot_id] -= sml.quantity
        return qties

    def _compute_moves_locations(self):
        # Split up moves by tracked quantities
        res = super()._compute_moves_locations()
        for wizard in self:
            for line in wizard.product_return_moves:
                qties = self._get_qty_by_lot(line.move_id)
                if qties is None:
                    continue
                first = True
                for lot, qty in qties.items():
                    if qty < 0:
                        continue
                    if first:
                        line.lot_id = lot
                        first = False
                    else:
                        line.copy({"lot_id": lot.id})
        return res

    def button_set_quantities(self):
        """Set quantities from wizard form"""
        self.ensure_one()
        self.set_quantities()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.act_stock_return_picking"
        )
        action["res_id"] = self.id
        return action

    def set_quantities(self, only_check=False):
        """Set, or check quantities to the quantities that were shipped out, per lot"""
        self.ensure_one()
        move2line = defaultdict(lambda: self.env["stock.return.picking.line"])
        for line in self.product_return_moves:
            move2line[line.move_id] += line

        for move, lines in move2line.items():
            qties = self._get_qty_by_lot(move)
            for line in lines:
                if line.lot_id not in qties:
                    raise UserError(
                        self.env._(
                            "Line with product %(product)s has lot %(lot)s but this "
                            "lot was not shipped out in the first place.",
                            product=line.product_id.name or "-",
                            lot=line.lot_id.name,
                        )
                    )
                if float_compare(
                    line.quantity,
                    qties[line.lot_id],
                    precision_rounding=line.product_id.uom_id.rounding,
                ) == 1 and not self.env.context.get(
                    CONTEXT_KEY_ACTIONS_CREATE_RETURNS_ALL
                ):
                    # Don't drop quantities silently in interactive mode
                    raise UserError(
                        self.env._(
                            "Line with product %(product)s and lot %(lot)s has "
                            "quantity %(quantity)s but this is higher than the "
                            "quantity that was shipped out in this lot "
                            "(%(shipped_quantity)s)",
                            product=line.product_id.name,
                            lot=line.lot_id.name or "-",
                            quantity=line.quantity,
                            shipped_quantity=qties[line.lot_id],
                        )
                    )
                if not only_check:
                    line.quantity = qties[line.lot_id]

    def action_create_returns_all(self):
        self = self.with_context(**{CONTEXT_KEY_ACTIONS_CREATE_RETURNS_ALL: True})
        return super().action_create_returns_all()

    def _create_return(self):
        if self.env.context.get(CONTEXT_KEY_ACTIONS_CREATE_RETURNS_ALL):
            self.set_quantities()
        else:
            self.set_quantities(only_check=True)
        picking = super()._create_return()
        for ml in picking.move_line_ids:
            ml.lot_id = ml.move_id.restrict_lot_id
        return picking
