from odoo import models, fields

class ProgramLearningOutcome(models.Model):
    _name = 'program.learning.outcome'
    _description = 'Program Learning Outcome'

    name = fields.Char(required=True)
    subdomain_id = fields.Many2one('program.learning.outcome.subdomain', required=True)
    course_outcome_ids = fields.One2many('course.outcome', 'plo_id', string="Course Outcomes")
