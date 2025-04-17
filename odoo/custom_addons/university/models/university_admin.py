from odoo import models, fields

class UniversityAdmin(models.Model):
    _name = 'admin'
    _description = 'University Admin'

    specialization = fields.Char(required=True)
    salary = fields.Char(required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    college_ids = fields.Many2many('college', string='Colleges')
    department_ids = fields.Many2many('department', string='Departments')

