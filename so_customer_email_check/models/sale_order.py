# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError

class SalesOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for order in self:
            if not order.website_id and not order.partner_id.email:
                raise UserError(
                    _("\nThe customer: %s doesn't have an email!\n\n Please add an email for the customer in order to confirm this order.") % (
                        order.partner_id.name))
        return super(SalesOrder, self).action_confirm()
