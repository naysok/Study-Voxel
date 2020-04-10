import time
from PIL import Image, ImageDraw

from operate_color import calc_color, image_processing, util

ut = util.UTIL()
im = image_processing.ImageProcessing()

resoluiton = 4
mode = None
color_correction = 0


path = "./_images_/color_gradation/master_1.png"



### mode 
# mode = "stratasys"

### color correction : 0
color_correction = 0.5





time1 = time.time()




new_image = im.put_cmyk(path, resoluiton, mode, color_correction)

# new_image.show()
new_image.save('_images_/dev.png', quality=100)




time2 = time.time()

print("python - time : {} sec".format(time2 - time1))