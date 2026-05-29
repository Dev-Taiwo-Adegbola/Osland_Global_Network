import imp
import os
import sys

# Set the path to your Django project directory
# This should be the directory containing manage.py
sys.path.insert(0, os.path.dirname(__file__))

# Import the WSGI application from your project's wsgi.py
# If your project is named 'osland', the module will be 'osland.wsgi'
from osland.wsgi import application as application

# Phusion Passenger (cPanel Python Selector) looks for 'application'
