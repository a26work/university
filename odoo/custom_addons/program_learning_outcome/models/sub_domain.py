from odoo import models, fields

class SubDomain(models.Model):
    _name = 'program_learning_outcome.sub_domain'
    _description = 'Sub Domain'

    name = fields.Char(required=True)
    domain_id = fields.Many2one('program_learning_outcome.domain', required=True)
    plo_ids = fields.One2many('program_learning_outcome.plo', 'sub_domain_id', string="PLOs")
