from odoo import models, fields

class Evaluation(models.Model):
    _name = 'evaluation'
    _description = 'Evaluation'

    name = fields.Char(string='Evaluation Title', required=True)
    score = fields.Float(string='Score', required=True)
    student_id = fields.Many2one('student', string='Student', required=True)


