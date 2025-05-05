# University Management System Module for Odoo 17

This module provides comprehensive functionality for managing universities, colleges, departments, programs, courses, students, and faculty within Odoo 17.

## Features

- **University Administration**: Manage university administrative details and settings
- **College Management**: Create and manage multiple colleges within a university
- **Department Structure**: Organize departments within colleges
- **Program Management**: Define academic programs with their requirements and curricula
- **Course Catalog**: Maintain a complete database of courses with descriptions and prerequisites
- **Student Information System**: Track student enrollment, academic records, and personal information
- **Faculty Management**: Manage doctor/faculty profiles, specializations, and teaching assignments

## Models

### Admin (`admin.py`)
- University administration settings
- System configuration
- User access management

### College (`college.py`)
- College information and structure
- Relationship with departments
- Administrative staff

### Department (`department.py`)
- Academic departments
- Department heads and staff
- Facilities and resources

### Program (`program.py`)
- Academic programs and degrees
- Program requirements
- Curriculum structure

### Course (`course.py`)
- Course catalog
- Course descriptions
- Credit hours and prerequisites

### Student (`student.py`)
- Student personal information
- Academic records
- Enrollment status

### Doctor (`doctor.py`)
- Faculty profiles
- Specializations
- Teaching assignments

## Installation

1. Download the module from the repository
2. Place it in your Odoo addons directory
3. Update the module list in Odoo
4. Install the module from the Apps menu

## Configuration

After installation:

1. Go to the University module in the main menu
2. Set up your colleges, departments, and programs
3. Define your course catalog
4. Add faculty members and students
5. Configure user access rights as needed

## Usage

The module provides a comprehensive interface for:
- Administrators to manage the university structure
- Faculty to manage courses and student records
- Students to view their academic information

## Dependencies

- Odoo 17 Base
- HR module (for faculty management)

