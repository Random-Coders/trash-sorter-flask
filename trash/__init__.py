"""
Imports
"""

# Flask imports
from flask import Flask
from flask_restful import Api
from trash import resources

# Create Flask app
app = Flask(__name__)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

api = Api(app)

# create API endpoints
api.add_resource(resources.PhotoUpload, '/api/trash/image/upload/<string:fname>')
api.add_resource(resources.WhichBin, 'api/trash/sort/<item>')
