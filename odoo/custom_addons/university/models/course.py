from odoo import models, fields

class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    program_ids = fields.Many2many('program', string='Program')
    outcome_ids = fields.One2many('course.outcome', 'course_id', string='Course Outcomes')

