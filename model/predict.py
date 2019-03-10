from clarifai.rest import ClarifaiApp
import constants

app = ClarifaiApp(api_key=constants.CLARIFAI_API)
model = app.models.get('trashsorter')
# model.model_version = '1.0'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('https://images-na.ssl-images-amazon.com/images/I/81Ui422yY9L._SL1500_.jpg')
# model.predict_by_filename()
print(response)