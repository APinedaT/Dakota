# -*- coding: utf-8 -*-

from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    module_test_operations = fields.Boolean('Test/Sample Orders')
