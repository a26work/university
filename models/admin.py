from odoo import models, fields

class Admin(models.Model):
    _name = 'admin'
    _description = 'University Admin'

    name = fields.Char(string='Student Name', required=True)
    specialization = fields.Char(required=True)
    salary = fields.Char(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    admin_id = fields.Char(string='Admin ID', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    college_ids = fields.Many2many('college', string='Colleges')
    department_ids = fields.Many2many('department', string='Departments')
    active = fields.Boolean(string='Active', default=True)
