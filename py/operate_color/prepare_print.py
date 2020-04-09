import math
import random
import time


from PIL import Image, ImageDraw

from . import util, calc_color



class PreparePrint():

    def open_img(self, path):
        img = Image.open(path)
        return img

    def get_size(self, path):
        img = Image.open(path)
        return img.size
    

    def create_canvas(self, canvas_size):
        new_image = Image.new("RGBA", canvas_size, (227, 233, 253, 255))
        return new_image
    

    def paste_image(self, base_image, paste_image, position):
        base_image.paste(paste_image, position)
        return base_image


    def add_shape(self,image, shape):

        width, height = image.size

        image_data = image.getdata()
        shape_data = shape.getdata()

        result_image = Image.new("RGBA", [width, height])

        for y in range(height):
            for x in range(width):
                if shape_data[y * width + x] == (0, 0, 0):
                    result_image.putpixel((x, y), (0, 0, 0, 255))
                else:
                    result_image.putpixel((x, y), image_data[y * width + x])

        return result_image