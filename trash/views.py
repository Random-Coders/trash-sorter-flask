from trash import app
from flask import render_template, redirect, url_for, request
from PIL import Image
from os import path

@app.route("/", methods=["GET"])
def home():
    return "hello there"

@app.route("/upload", methods=["POST"])
def upload():
    img = Image.open(request.files['file'])
    f = path.join(app.config['UPLOAD_FOLDER'], 'image.png')
    img.save(f)
    return 'Image saved Success!'
