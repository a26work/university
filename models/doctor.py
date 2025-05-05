from odoo import models, fields

class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    specialization = fields.Char(required=True)
    qualification = fields.Selection([
        ('assistant', 'Assistant Professor'),
        ('associate', 'Associate Professor'),
        ('professor', 'Full Professor'),
        ('lecturer', 'Lecturer'),
        ('adjunct', 'Adjunct Professor')
    ], string='Qualification', tracking=True)
    salary = fields.Char(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    doctor_id = fields.Char(string='Doctor ID', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    course_ids = fields.Many2many('course', string='Courses')
    active = fields.Boolean(string='Active', default=True)
