from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import constants

app = ClarifaiApp(api_key=constants.CLARIFAI_API)

# add multiple images with concepts
img1 = ClImage(filename="data/train/cardboard/cardboard1.jpg", concepts=['boscoe'], not_concepts=['our_wedding'])
img2 = ClImage(url="https://samples.clarifai.com/wedding.jpg", concepts=['our_wedding'], not_concepts=['cat','boscoe'])


app.inputs.bulk_create_images([img1, img2])