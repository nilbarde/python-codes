from PIL import Image

read_name = '1.png'
write_name = '2.png'

img = Image.open(read_name)

#img = img.transpose( Image.FLIP_LEFT_RIGHT )
img = img.transpose( Image.FLIP_TOP_BOTTOM )

img.save(write_name)




