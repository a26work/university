from odoo import models, fields

class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    program_ids = fields.Many2many('program', string='Program')
    active = fields.Boolean(string='Active', default=True)

    credit_hours = fields.Float(string='Credit Hours', required=True)
    lecture_hours = fields.Float(string='Lecture Hours Per Week', required=True)
    lab_hours = fields.Float(string='Lab Hours Per Week', default=0.0)

    sections_count = fields.Integer(string='Number of Sections', default=1,
                                    help='Number of sections to be created for this course')

    section_duration = fields.Float(string='Section Duration (Hours)', default=1.5,
                                    help='Duration of each section in hours')

    preferred_time_of_day = fields.Selection([
        ('early', 'Early Morning (8:00-11:00)'),
        ('mid', 'Mid Day (11:00-14:00)'),
        ('afternoon', 'Afternoon (14:00-17:00)'),
        ('evening', 'Evening (17:00-20:00)')
    ], string='Preferred Time of Day')

    # Hall requirements
    min_hall_capacity = fields.Integer(string='Minimum Hall Capacity', default=30)
    requires_projector = fields.Boolean(string='Requires Projector', default=False)
    requires_computer = fields.Boolean(string='Requires Computer', default=False)
    requires_internet = fields.Boolean(string='Requires Internet', default=False)
    requires_special_equipment = fields.Boolean(string='Requires Special Equipment', default=False)
    special_equipment_desc = fields.Text(string='Special Equipment Description')

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Course code must be unique!')
    ]
