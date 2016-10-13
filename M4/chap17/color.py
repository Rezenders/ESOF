from PIL import ImageColor
from PIL import Image

catIm = Image.open('zophie.png')
print (catIm)
print (catIm.size)
width, height = catIm.size
print (width, height)
print (catIm.filename)
print (catIm.format)
print (catIm.format_description)
catIm.save('zophie.jpg')

im = Image.new('RGBA',(100,200), 'purple')
im.save('purpleImage.png')

im2 = Image.new('RGBA', (20,20))
im2.save( 'transparentImage.png')

faceIm = catIm.crop((335, 345, 565, 560))
faceIm.save('cropped.png')

catCopyIm = catIm.copy()
catCopyIm.paste(faceIm, (0,0))
catCopyIm.paste(faceIm, (400,500))
catCopyIm.save('pasted.png')

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight =  faceIm.size
catCopyTwo = catIm.copy()

for left in range(0,catImWidth, faceImWidth):
	for top in range(0, catImHeight, faceImHeight):
		print(left,top)
		catCopyTwo.paste(faceIm, (left,top))

catCopyTwo.save('allcats.png')

quartersizedIm = catIm.resize((int(catImWidth/2), int(catImHeight/2)))
quartersizedIm.save('quartersized.png')

svelteIm = catIm.resize((catImWidth, catImHeight + 300))
svelteIm.save('svelte.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')





