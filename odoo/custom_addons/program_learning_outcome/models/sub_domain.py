from odoo import models, fields

class ProgramLearningOutcomeSubDomain(models.Model):
    _name = 'program.learning.outcome.subdomain'
    _description = 'Sub Domain'

    name = fields.Char(required=True)
    domain_id = fields.Many2one('program_learning_outcome.domain', required=True)
    plo_ids = fields.One2many('program.learning.outcome', 'subdomain_id', string="PLOs")
