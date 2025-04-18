{
    'name': 'University Management',
    'author': 'Author Name',
    'category': '',
    'version': '17.0.0.1.0',
    'summary': 'Manage colleges, departments, programs, courses, and outcomes',
    'description': 'A module to manage university structure including colleges, departments, programs, courses and learning outcomes.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_views.xml',
        'views/college_views.xml',
        'views/department_views.xml',
        'views/program_views.xml',
        'views/course_views.xml',
        'views/course_outcome_views.xml',
        'views/student_views.xml',
        'views/doctor_views.xml',
        'views/admin_views.xml',
        'views/evaluation_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
