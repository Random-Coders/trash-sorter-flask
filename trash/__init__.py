"""
Imports
"""

# Flask imports
from flask import Flask

# Create Flask app
app = Flask(__name__, template_folder='templates')

# Add Configurations to app
app.config.from_pyfile('config.py', silent=False)

from trash import views
