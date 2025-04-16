from odoo import models, fields

class CourseOutcome(models.Model):
    _name = 'university.course.outcome'
    _description = 'Course Outcome'

    name = fields.Char(required=True)
    course_id = fields.Many2one('university.course', string='Course', required=True)


