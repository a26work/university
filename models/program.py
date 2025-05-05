from odoo import models, fields, api

class Program(models.Model):
    _name = 'program'
    _description = 'Academic Program'

    name = fields.Char(string='Program Name', required=True)
    code = fields.Char(string='Program Code', required=True)
    degree = fields.Selection([
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master')
    ], string='Degree Level', required=True)
    department_id = fields.Many2one('department', string='Department', required=True)
    course_ids = fields.Many2many('course', 'program_id', string='Courses')
    active = fields.Boolean(string='Active', default=True)

    @api.depends('department_id')
    def _compute_college(self):
        for program in self:
            program.college_id = program.department_id.college_id

    college_id = fields.Many2one('college', string='College', compute='_compute_college', store=True)
