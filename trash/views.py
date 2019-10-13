from trash import app
from flask import render_template, redirect, url_for, request, Flask
from PIL import Image
from os import path
import json
from PIL import Image
import requests
from io import BytesIO 
from clarifai.rest import ClarifaiApp

# app = Flask(__name__)

capp = ClarifaiApp(api_key='fa54b65808c746f6a0d3a71cf2457bc9')
model = capp.models.get('trashsorter')

@app.route("/sort/<url>", methods=["GET", "POST"])
def download(url):
	print(url)
	response = model.predict_by_url(url)
	return json.dumps(response)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    img = Image.open(request.files['file'])
    f = path.join(app.config['UPLOAD_FOLDER'], 'image.png')
    img.save(f)
    return 'Success!'

