from odoo import models, fields, api
import base64
import qrcode
from io import BytesIO

class AccountMove(models.Model):
    _inherit = 'account.move'

    qr_code = fields.Binary(string="QR Code", compute="_compute_qr_code", store=True)

    @api.depends('name', 'amount_total', 'invoice_date')
    def _compute_qr_code(self):
        for record in self:
            data = f"Invoice: {record.name}\nTotal: {record.amount_total}\nDate: {record.invoice_date}"
            qr = qrcode.make(data)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            record.qr_code = base64.b64encode(buffer.getvalue())

