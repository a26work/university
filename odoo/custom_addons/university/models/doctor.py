from odoo import models, fields

class Doctor(models.Model):
    _name = 'university.doctor'
    _description = 'Doctor'

    specialization = fields.Char(required=True)
    salary = fields.Char(required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    course_ids = fields.Many2many('university.course', string='Courses')

