# program_learning_outcome/models/course_outcome_inherit.py
from odoo import models, fields

class CourseOutcome(models.Model):
    _inherit = 'course.outcome'

    plo_id = fields.Many2one('program.learning.outcome', string="PLO")
