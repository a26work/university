from odoo import models, fields

class Evaluation(models.Model):
    _name = 'university.evaluation'
    _description = 'Evaluation'

    name = fields.Char(string='Evaluation Title', required=True)
    score = fields.Float(string='Score', required=True)
    student_id = fields.Many2one('university.student', string='Student', required=True)


