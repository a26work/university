from odoo import models, fields

class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Department Code', required=True)
    college_id = fields.Many2one('college', string='College', required=True)
    program_ids = fields.One2many('program', 'department_id', string='Programs')
    admin_ids = fields.Many2many('admin', string='Admins')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Department code must be unique!')
    ]
