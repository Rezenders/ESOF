from PIL import Image
import os

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIM = Image.open(LOGO_FILENAME)
logoIM = logoIM.resize((int(808/10),int(768/10)))
logoWidth, logoHeight = logoIM.size
print (logoWidth, logoHeight)

os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
		continue
	
	im = Image.open(filename)
	width, height = im.size
	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
		if width> height:
			height = int((SQUARE_FIT_SIZE / width) * height)
			width = SQUARE_FIT_SIZE
		else:
			width = int((SQUARE_FIT_SIZE / height) * width)
			height = SQUARE_FIT_SIZE
		im = im.resize( (width,height))
			
	im.paste(logoIM, (width-logoWidth, height - logoHeight), logoIM)
	im.save('withLogo/'+filename)
