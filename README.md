
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=18.0)
[![Pre-commit Status](https://github.com/OCA/stock-logistics-workflow/actions/workflows/pre-commit.yml/badge.svg?branch=18.0)](https://github.com/OCA/stock-logistics-workflow/actions/workflows/pre-commit.yml?query=branch%3A18.0)
[![Build Status](https://github.com/OCA/stock-logistics-workflow/actions/workflows/test.yml/badge.svg?branch=18.0)](https://github.com/OCA/stock-logistics-workflow/actions/workflows/test.yml?query=branch%3A18.0)
[![codecov](https://codecov.io/gh/OCA/stock-logistics-workflow/branch/18.0/graph/badge.svg)](https://codecov.io/gh/OCA/stock-logistics-workflow)
[![Translation Status](https://translation.odoo-community.org/widgets/stock-logistics-workflow-18-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/stock-logistics-workflow-18-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# Stock Workflow

Enhance the way flows and processes are working. Find here modules that do not have their place in the other more specialized repositories.

Are you looking for modules related to logistics? Or would like to contribute
to? There are many repositories with specific purposes. Have a look at this
[README](https://github.com/OCA/wms/blob/18.0/README.md).

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[delivery_procurement_group_carrier](delivery_procurement_group_carrier/) | 18.0.1.0.0 |  | Delivery Procurement Group Carrier
[sale_order_global_stock_route](sale_order_global_stock_route/) | 18.0.1.0.0 |  | Add the possibility to choose one warehouse path for an order
[stock_account_product_run_fifo_hook](stock_account_product_run_fifo_hook/) | 18.0.1.0.1 |  | Add more flexibility in the run fifo method.
[stock_dangerous_goods](stock_dangerous_goods/) | 18.0.1.0.0 | [![mmequignon](https://github.com/mmequignon.png?size=30px)](https://github.com/mmequignon) | Adds utility fields to manage dangerous goods
[stock_no_negative](stock_no_negative/) | 18.0.1.0.1 |  | Disallow negative stock levels by default
[stock_owner_restriction](stock_owner_restriction/) | 18.0.1.0.0 |  | Do not reserve quantity with assigned owner
[stock_picking_auto_create_lot](stock_picking_auto_create_lot/) | 18.0.1.0.0 | [![sergio-teruel](https://github.com/sergio-teruel.png?size=30px)](https://github.com/sergio-teruel) | Auto create lots for incoming pickings
[stock_picking_back2draft](stock_picking_back2draft/) | 18.0.1.0.0 |  | Reopen canceled transfers
[stock_picking_backorder_strategy_cancel](stock_picking_backorder_strategy_cancel/) | 18.0.1.0.0 | [![rousseldenis](https://github.com/rousseldenis.png?size=30px)](https://github.com/rousseldenis) [![mgosai](https://github.com/mgosai.png?size=30px)](https://github.com/mgosai) | Picking backordering strategies
[stock_picking_group_by_base](stock_picking_group_by_base/) | 18.0.1.0.0 |  | Allows to define a way to create index on extensible domain
[stock_picking_invoice_link](stock_picking_invoice_link/) | 18.0.1.0.0 |  | Adds link between pickings and invoices
[stock_picking_partner_note](stock_picking_partner_note/) | 18.0.1.0.0 |  | Add partner notes on picking
[stock_picking_purchase_order_link](stock_picking_purchase_order_link/) | 18.0.1.0.0 |  | Link between picking and purchase order
[stock_picking_return_restricted_qty](stock_picking_return_restricted_qty/) | 18.0.1.0.0 |  | Restrict the return to delivered quantity
[stock_picking_sale_order_link](stock_picking_sale_order_link/) | 18.0.1.0.0 |  | Link between picking and sale order
[stock_picking_show_backorder](stock_picking_show_backorder/) | 18.0.1.0.0 |  | Provides a new field on stock pickings, allowing to display the corresponding backorders.
[stock_picking_show_return](stock_picking_show_return/) | 18.0.1.0.0 |  | Show returns on stock pickings
[stock_picking_whole_scrap](stock_picking_whole_scrap/) | 18.0.1.0.0 | [![sergio-teruel](https://github.com/sergio-teruel.png?size=30px)](https://github.com/sergio-teruel) | Create whole scrap from a picking for move lines
[stock_split_picking](stock_split_picking/) | 18.0.1.0.0 |  | Split a picking in two not transferred pickings

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
