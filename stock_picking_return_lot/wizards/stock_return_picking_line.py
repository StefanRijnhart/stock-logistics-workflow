# Copyright 2024 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockReturnPickingLine(models.TransientModel):
    _inherit = "stock.return.picking.line"
    _sql_constraints = [
        (
            "lot_id_move_id_uniq",
            "UNIQUE(wizard_id, lot_id, move_id)",
            "The same lot cannot be used on multiple lines for the same move",
        )
    ]

    lot_id = fields.Many2one(
        "stock.lot",
        string="Lot/Serial Number",
        domain="[('product_id', '=', product_id)]",
    )

    def _prepare_move_default_values(self, picking):
        # Set the wizard line lot as the move's restricted lot
        vals = super()._prepare_move_default_values(picking)
        vals["restrict_lot_id"] = self.lot_id.id
        return vals
