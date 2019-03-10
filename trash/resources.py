from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug

class UploadAudio(Resource):
  def post(self):
    parse = reqparse.RequestParser()
    parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    args = parse.parse_args()
    audioFile = args['file']
    audioFile.save("your_file_name.jpg")IdentifyTrash():
