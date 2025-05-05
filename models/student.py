from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    enrollment_date = fields.Date(string='Enrollment Date')
    graduation_date = fields.Date(string='Expected Graduation Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    level  = fields.Char(string='Level', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    program_id = fields.Many2one('program', string='Program', required=True)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('student_id_unique', 'UNIQUE(student_id)', 'Student ID must be unique!')
    ]
