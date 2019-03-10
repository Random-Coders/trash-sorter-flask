from clarifai.rest import ClarifaiApp
import constants

app = ClarifaiApp(api_key=constants.CLARIFAI_API)
model = app.models.get('rafs')
# model.model_version = '1.0'  # This is optional. Defaults to the latest model version.

response = model.predict_by_url('https://static.scientificamerican.com/sciam/cache/file/D059BC4A-CCF3-4495-849ABBAFAED10456_source.jpg?w=590&h=800&526ED1E1-34FF-4472-B348B8B4769AB2A1')
# model.predict_by_filename()
print(response)