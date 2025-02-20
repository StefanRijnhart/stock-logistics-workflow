# © 2016 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_back_to_draft(self):
        self.move_ids.action_back_to_draft()
