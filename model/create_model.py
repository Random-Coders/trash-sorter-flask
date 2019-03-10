from clarifai.rest import ClarifaiApp
import constants

app = ClarifaiApp(api_key=constants.CLARIFAI_API)
model = app.models.create('rafs', concepts=['boscoe'])