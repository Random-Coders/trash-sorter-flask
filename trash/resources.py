from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug, os

parser = reqparse.RequestParser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')


class PhotoUpload(Resource):
    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No file found',
                    'status':'error'
                    }
        photo = data['file']

        if photo:
            filename = 'image_to_indentify.png'
            photo.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data':'',
                    'message':'photo uploaded',
                    'status':'success'
                    }
        return {
                'data':'',
                'message':'Something when wrong',
                'status':'error'
                }

class WhichBin(Resource):
    pass
