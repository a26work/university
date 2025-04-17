from odoo import models, fields

class ProgramLearningOutcomeDomain(models.Model):
    _name = 'program.learning.outcome.domain'
    _description = 'Learning Domain'

    name = fields.Char(required=True)
    subdomain_ids = fields.One2many('program.learning.outcome.subdomain', 'domain_id', string="Sub Domains")
    program_id = fields.Many2one('university.program', string="Program")
