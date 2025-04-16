# program_learning_outcome/models/course_outcome_inherit.py
from odoo import models, fields

class CourseOutcome(models.Model):
    _inherit = 'university.course.outcome'

    plo_id = fields.Many2one('program_learning_outcome.plo', string="PLO")
