import sys; sys.path.append('..')
from conf import *

project = 'Python Shell Dec 2020'
author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'

todo_emit_warnings = True
todo_include_todos = False

html_static_path = ['../_static']
html_favicon = '../_static/favicon.png'

suppress_warnings += [
    'ref.ref',
]

master_doc = 'index'
