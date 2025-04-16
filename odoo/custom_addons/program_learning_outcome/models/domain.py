from odoo import models, fields

class Domain(models.Model):
    _name = 'program_learning_outcome.domain'
    _description = 'Learning Domain'

    name = fields.Char(required=True)
    sub_domain_ids = fields.One2many('program_learning_outcome.sub_domain', 'domain_id', string="Sub Domains")
    program_id = fields.Many2one('university.program', string="Program")
