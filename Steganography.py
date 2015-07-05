from PIL import Image


medium = Image.open('Images/MonaLisa.jpg')
#medium.show()
pixels = medium.load()
width, height = medium.size

pixel_list = []
for y in range(height):
	for x in range(width):
		#test = str(x) + ':' + str(y)
		pixel = pixels[x, y] 
		pixel_list.append(pixel)

new_pixel_list = []
for p in pixel_list:
	new_pixel = []
	for band in p:
		new_pixel.append(255-band)
	new_pixel_list.append(tuple(new_pixel))

new_img = Image.new(medium.mode, medium.size)
new_img.putdata(new_pixel_list)
new_img.save('Images/test.jpg')