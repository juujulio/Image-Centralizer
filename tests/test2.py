from PIL import Image, ImageOps

class Deformer():
    def getmesh(self, img):
        w, h = img.size
        # define a shape in the original image
        source_shape = (172, 8, 172, 136, 374, 136, 374, 8)
        # define a rectangle in the new image
        target_rect = (0, 0, 202, 128)  # left, top, right, bottom
        #return all the shapes
        return [(target_rect, source_shape)]

image = Image.open('image1.png')
deform = ImageOps.deform(image, Deformer())
deform.show()