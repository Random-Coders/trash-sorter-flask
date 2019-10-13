from clarifai.rest import ClarifaiApp
import os
#import constants

app = ClarifaiApp(api_key=os.environ['CLARIFAICONSTANT'])
model = app.models.get('trashsorter')
# model.model_version = '1.0'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2ChocolateChipCookies.jpg/1200px-2ChocolateChipCookies.jpg')
# model.predict_by_filename()
print(response)