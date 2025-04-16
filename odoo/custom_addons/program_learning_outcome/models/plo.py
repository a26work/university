from odoo import models, fields

class PLO(models.Model):
    _name = 'program_learning_outcome.plo'
    _description = 'Program Learning Outcome'

    name = fields.Char(required=True)
    sub_domain_id = fields.Many2one('program_learning_outcome.sub_domain', required=True)
    course_outcome_ids = fields.One2many('university.course.outcome', 'plo_id', string="Course Outcomes")
