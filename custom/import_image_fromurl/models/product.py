# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

import logging
# from openerp.osv import osv, fields
# from openerp import tools
import requests

_logger = logging.getLogger(__name__)
try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    image_url = fields.Char('IMAGE URL:')

    @api.multi
    def write(self, vals):
        for obj in self:
            if vals.get('image_url'):
                img = vals.get('image_url')
                log_val = {
                    'object': 'Product',
                    'resource_id': obj.id,
                    'result': 'success',
                }
                if 'https' in vals.get('image_url'):
                    img = vals.get('image_url').replace("https", "http")
                try:
                    binary_data = tools.image_resize_image_big(base64.b64encode(requests.get(img).content))
                    vals.update({'image': binary_data})
                except Exception as e:
                    log_val.update({
                        'result': 'error',
                        'error_message': str(e),
                    })
                self.env['import.image.url.log'].create(log_val)
        return super(ProductTemplate, self).write(vals)

    @api.model
    def create(self, vals):
        if vals.get('image_url'):
            img = vals.get('image_url')
            log_val = {
                'object': 'Product',
                'resource_id': None,
                'result': 'success',
            }
            if 'https' in vals.get('image_url'):
                    img = vals.get('image_url').replace("https", "http")
            try:
                binary_data = tools.image_resize_image_big(base64.b64encode(requests.get(img).content))
                vals.update({'image': binary_data})
            except Exception as e:
                log_val.update({
                    'result': 'error',
                    'error_message': str(e),
                })
            self.env['import.image.url.log'].create(log_val)
        return super(ProductTemplate, self).create(vals)

