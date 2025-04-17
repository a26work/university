from odoo import models, fields

class Program(models.Model):
    _name = 'program'
    _description = 'Program'

    name = fields.Char(required=True)
    department_id = fields.Many2one('department', string='Department', required=True)
    course_ids = fields.Many2many('course', string='Courses')
