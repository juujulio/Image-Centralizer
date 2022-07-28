from PIL import Image

# create new image by import
image = Image.open('image1.png')

# create a new image from scratch
image_blank = Image.new('RGBA', (1000, 600))

# show the picture
image_blank.show()

# saving the picture
# image.save('test_save', format = 'png')


