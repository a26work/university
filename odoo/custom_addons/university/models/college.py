from odoo import models, fields

class College(models.Model):
    _name = 'university.college'
    _description = 'College'

    name = fields.Char(required=True)
    department_ids = fields.One2many('university.department', 'college_id', string='Departments')
    admin_ids = fields.Many2many('university.admin', string='Admins')

