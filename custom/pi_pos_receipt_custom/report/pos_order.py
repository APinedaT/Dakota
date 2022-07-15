from odoo import fields,models,api,_

class pos_order(models.Model):
    _inherit = "pos.order"
    
    @api.multi
    def print_pi_pos_receipt_custom(self):
        return self.env.ref('pi_pos_receipt_custom.action_print_pi_pos_receipt_custom').report_action(self)