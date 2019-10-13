from trash import app
from flask import render_template, redirect, url_for, request, Flask
from PIL import Image
from os import path
import json
from PIL import Image
import requests
from io import BytesIO 
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

# app = Flask(__name__)

capp = ClarifaiApp(api_key='fa54b65808c746f6a0d3a71cf2457bc9')
model = capp.models.get('trashsorter')

@app.route("/sort", methods=["GET", "POST"])
def sort():
    if request.method == "POST":
        if request.files:
            img = Image.open(request.files['trash_pic'])
            img.thumbnail((300,300), Image.ANTIALIAS)
            f = path.join(app.config['UPLOAD_FOLDER'], 'image.png')
            img.save(f)
            res = model.predict_by_filename(path.join(app.config['UPLOAD_FOLDER'], 'image.png'))
            print(res['output']['data'])
            place = ''
            if response == 'plastic':
                place = 'recycle'
            elif response == 'cardboard':
                place = 'compost'
            elif response == 'paper':
                place = 'recycle'
            elif response == 'metal':
                place = 'trash'
            elif response == 'trash':
                place = 'trash'
            elif response == 'glass':
                place = 'recycle'
           	else:
           	    raise Exception
            return render_template('index.html', var=place)
    return render_template('index.html', var=None)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', var=None)

@app.route("/upload", methods=["POST"])
def upload():
    img = Image.open(request.files['file'])
    f = path.join(app.config['UPLOAD_FOLDER'], 'image.png')
    img.save(f)
    return 'Success!'

