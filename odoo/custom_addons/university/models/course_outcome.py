from odoo import models, fields

class CourseOutcome(models.Model):
    _name = 'course.outcome'
    _description = 'Course Outcome'

    name = fields.Char(required=True)
    course_id = fields.Many2one('course', string='Course', required=True)


