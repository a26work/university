from odoo import models, fields

class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Char(required=True)
    college_id = fields.Many2one('college', string='College', required=True)
    program_ids = fields.One2many('program', 'department_id', string='Programs')
    admin_ids = fields.Many2many('admin', string='Admins')

