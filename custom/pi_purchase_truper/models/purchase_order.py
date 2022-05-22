# -*- coding: utf-8 -*-

from odoo import models, fields
import csv
import base64
import time

class PiPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    csv_truper = fields.Binary()
    name_file_truper = fields.Char()

    def button_truper(self):
        order_lines = self.order_line
        with open('/tmp/export.tsv', 'w') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(['710683'])
            for line in order_lines:
                codigo = line.product_id.default_code
                codigo_truper = codigo.replace(" TR","")
                qty = int(line.product_qty)
                tsv_writer.writerow([codigo_truper, qty])
        with open('/tmp/export.tsv', 'r', encoding="utf-8") as f2:
            # file encode and store in a variable ‘data’
            data = str.encode(f2.read(), 'utf-8')
        self.csv_truper = base64.encodestring(data)
        self.name_file_truper = 'export.tsv'

        return {
            'type': 'ir.actions.act_url',
            'url': "web/content/?model=purchase.order&id=" + str(self.id) +
                    "&filename=export.tsv&field=csv_truper&download=true&filename=" + self.name_file_truper,
            'target': 'new',
        }
        