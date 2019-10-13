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

def max_concept(l):
    max_confidence = 0
    best_concept = None
    for concept in l:
        if concept['value'] > max_confidence:
            best_concept = concept['name']
    return best_concept

@app.route("/sort", methods=["GET", "POST"])
def sort():
    if request.method == "POST":
        if request.files:
            img = Image.open(request.files['trash_pic'])
            img.thumbnail((300,300), Image.ANTIALIAS)
            f = path.join(app.config['UPLOAD_FOLDER'], 'image.png')
            img.save(f)
            res = model.predict_by_filename(path.join(app.config['UPLOAD_FOLDER'], 'image.png'))
            print(res['outputs'][0]['data']['concepts'])
            type_of_trash = max_concept(res['outputs'][0]['data']['concepts'])
            print(type_of_trash)
            print(res['output']['data'])
            place = ''
            if type_of_trash == 'plastic':
            	place = 'recycle'
            elif type_of_trash == 'cardboard':
            	place = 'compost'
            elif type_of_trash == 'paper':
            	place = 'recycle'
            elif type_of_trash == 'metal':
            	place = 'trash'
            elif type_of_trash == 'trash':
            	place = 'trash'
            elif type_of_trash == 'glass':
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

