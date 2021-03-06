from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os

app = ClarifaiApp(api_key=os.environ['CLARIFAICONSTANT'])

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

cardboard_imgs = os.listdir('data/train/cardboard')
cardboard_imgs = list(chunks(cardboard_imgs, 128))
for split_cardboard_imgs in cardboard_imgs:
	imgs = []
	for img_name in split_cardboard_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/cardboard/{img_name}", concepts=["cardboard"], not_concepts=["glass", "metal", "plastic", "trash"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)

glass_imgs = os.listdir('data/train/glass')
glass_imgs = list(chunks(glass_imgs, 128))
for split_glass_imgs in glass_imgs:
	imgs = []
	for img_name in split_glass_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/glass/{img_name}", concepts=["glass"], not_concepts=["cardboard", "metal", "paper", "trash"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)

metal_imgs = os.listdir('data/train/metal')
metal_imgs = list(chunks(metal_imgs, 128))
for split_metal_imgs in metal_imgs:
	imgs = []
	for img_name in split_metal_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/metal/{img_name}", concepts=["metal"], not_concepts=["glass", "cardboard", "paper", "plastic", "trash"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)

paper_imgs = os.listdir('data/train/paper')
paper_imgs = list(chunks(paper_imgs, 128))
for split_paper_imgs in paper_imgs:
	imgs = []
	for img_name in split_paper_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/paper/{img_name}", concepts=["paper"], not_concepts=["glass", "metal", "plastic", "trash"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)

trash_imgs = os.listdir('data/train/trash')
trash_imgs = list(chunks(trash_imgs, 128))
for split_trash_imgs in trash_imgs:
	imgs = []
	for img_name in split_trash_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/trash/{img_name}", concepts=["trash"], not_concepts=["glass", "metal", "plastic", "paper", "cardboard"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)

plastic_imgs = os.listdir('data/train/plastic')
plastic_imgs = list(chunks(plastic_imgs, 128))
for split_plastic_imgs in plastic_imgs:
	imgs = []
	for img_name in split_plastic_imgs:
		print(img_name)
		if img_name == ".DS_Store":
			continue
		img = ClImage(filename=f"data/train/plastic/{img_name}", concepts=["plastic"], not_concepts=["glass", "metal", "paper", "cardboard"])
		imgs.append(img)
	app.inputs.bulk_create_images(imgs)



