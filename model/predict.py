from clarifai.rest import ClarifaiApp
import os
#import constants

app = ClarifaiApp(api_key=os.environ['CLARIFAICONSTANT'])
model = app.models.get('trashsorter')
# model.model_version = '1.0'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('http://www.recyclinggame.colostate.edu/images/chips.png')
# model.predict_by_filename()
print(response)