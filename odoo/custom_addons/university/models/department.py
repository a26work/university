from odoo import models, fields

class Department(models.Model):
    _name = 'university.department'
    _description = 'Department'

    name = fields.Char(required=True)
    college_id = fields.Many2one('university.college', string='College', required=True)
    program_ids = fields.One2many('university.program', 'department_id', string='Programs')
    admin_ids = fields.Many2many('university.admin', string='Admins')

