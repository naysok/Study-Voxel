import time

from operate_color import calc_color, image_processing, util

ut = util.UTIL()
im = image_processing.ImageProcessing()

resoluiton = 4
path = "./_images_/master.png"

im.put_cmyk(path, resoluiton)


# v = ut.set_vector(resoluiton)
# print(v)


# time1 = time.time()
# time2 = time.time()
# time3 = time.time()

# time_a  = time2 - time1
# time_b  = time3 - time2

# print("python - time : {} sec".format(time_a))
# print("cython - time : {} sec".format(time_b))