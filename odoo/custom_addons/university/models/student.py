from odoo import models, fields

class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    level  = fields.Char(required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    program_id = fields.Many2one('university.program', string='Program', required=True)
    evaluation_ids = fields.One2many('university.evaluation', 'student_id', string='Evaluations')

