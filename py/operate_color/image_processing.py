import math
import random
import time


from PIL import Image, ImageDraw

import calc_color_fast as cf

from . import util, calc_color



class ImageProcessing():

    def get_color_to_memory(self, image):
        size = image.size
        cl_l = []
        for i in range(size[0]):
            cl = []
            for j in range(size[1]):
                c = image.getpixel((i, j))
                cl.append(c)
            cl_l.append(cl)
        return cl_l


    def calc_rgb_cmyk(self, rgb):
        if len(rgb) == 4:
             new_rgb = [rgb[0], rgb[1], rgb[2]]
        else:
            new_rgb = rgb
        a, b = cf.rgb_to_cmyk(rgb)

        return b


    def calc_cmyk_count(self, cmyk, res):
        c, m, y, k = cmyk
        sum_ = 400

        cc = round((c / sum_) * (res*res))
        mm = round((m / sum_) * (res*res))
        yy = round((y / sum_) * (res*res))
        kk = round((k / sum_) * (res*res))

        return [cc, mm, yy, kk]


    def calc_cmy_count(self, cmyk, res, cc):
        c, m, y, k = cmyk
        sum_ = 300

        ### Color Correction = 0
        color_correction = cc
        cc = round(((c / sum_) * (res*res)) + color_correction)
        mm = round(((m / sum_) * (res*res)) + color_correction)
        yy = round(((y / sum_) * (res*res)) + color_correction)

        return [cc, mm, yy]


    def up_scale(self, image, res):
        ### "VeroClear", 227, 233, 253
        _size = image.size
        new_image = Image.new("RGBA", (_size[0] * res, _size[1] * res), (227, 233, 253, 255))
        return new_image


    def put_cmyk(self, path, res, mode, color_correction):

        """
        ### Stratasys_J750
        ["VeroBlack", 26, 26, 29]
        ["VeroCyan", 0, 90, 158]
        ["VeroMgnt", 166, 33, 98]
        ["VeroYellow", 200, 189, 3]
        """

        ### Stratasys_J750
        if mode == "stratasys":
            _c_ = (0, 90, 158, 255)
            _m_ = (166, 33, 98, 255)
            _y_ = (200, 189, 3, 255)
            _k_ = (26, 26, 29, 255)

        ### cmyk
        else:
            _c_ = (0, 255, 255, 255)
            _m_ = (255, 0, 255, 255)
            _y_ = (255, 255, 0, 255)
        


        ut = util.UTIL()
        
        image = Image.open(path)
        image_size = image.size

        clr_list = self.get_color_to_memory(image)

        # print("Memory : ", ut.ll_size(clr_list))

        new_image  = self.up_scale(image, res)
        new_image_size = new_image.size
        
        # print("PIL : ", image_size)
        # print(new_image_size)

        vectors = ut.set_vector(res)

        for i in range(image_size[0]):
            for j in range(image_size[1]):

                pt = (i * res, j * res)
                rgb = clr_list[i][j]
                new_vectors = random.sample(vectors, len(vectors))

                cmyk = self.calc_rgb_cmyk(rgb)


                ### ========== CMYK ==========
                # cc, mm, yy, kk = self.calc_cmyk_count(cmyk, res)
                # new_length = cc + mm + yy + kk
                ### ========== CMYK ==========


                ### ========== CMY ==========
                cc, mm, yy = self.calc_cmy_count(cmyk, res, color_correction)
                _length = cc + mm + yy
                ### ========== CMY ==========


                if _length > (res * res):
                    new_length = (res * res)
                else:
                    new_length = _length

                new_pt = []

                for k in range(new_length):

                    new_pt = ut.pt2d_add(pt, new_vectors[k])
                    # print(new_pt)

                    if k < cc:
                        new_image.putpixel(new_pt, (_c_))
                    elif k < (cc + mm):
                        new_image.putpixel(new_pt, (_m_))
                    elif k < (cc + mm + yy):
                        new_image.putpixel(new_pt, (_y_))
                    # else:
                    #     new_image.putpixel(new_pt, (_k_))
        
        # new_image.show()
        new_image.save('_images_/dev.png', quality=100)

        
        # return new_image