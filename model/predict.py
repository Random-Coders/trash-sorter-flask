from clarifai.rest import ClarifaiApp
import os
#import constants

app = ClarifaiApp(api_key=os.environ['CLARIFAICONSTANT'])
model = app.models.get('trashsorter')
# model.model_version = '1.0'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('https://github.com/Random-Coders/trash-sorter-flask/blob/raftesting/CF91DF25-0ED4-48D8-9502-3595FE4CE427_1_105_c.jpeg?raw=true')
# model.predict_by_filename()
print(response)