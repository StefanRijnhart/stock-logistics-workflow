# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock Restrict Lot",
    "summary": "Base module that add back the concept of restrict lot on stock move",
    "version": "17.0.1.1.0",
    "category": "Warehouse Management",
    "website": "https://github.com/OCA/stock-logistics-workflow",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["florian-dacosta"],
    "license": "LGPL-3",
    "installable": True,
    "depends": ["stock"],
    "data": ["views/stock_move_views.xml", "views/stock_picking.xml"],
}
