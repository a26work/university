from odoo import models, fields

class College(models.Model):
    _name = 'college'
    _description = 'College'

    name = fields.Char(required=True)
    department_ids = fields.One2many('department', 'college_id', string='Departments')
    admin_ids = fields.Many2many('admin', string='Admins')

