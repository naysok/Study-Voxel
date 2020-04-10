import time


from operate_color import calc_color, image_processing, util, prepare_print


ut = util.UTIL()
pp = prepare_print.PreparePrint()


shape_path = "./_images_/200409_sphere/contour_400/"
color_path = "./_images_/200409_sphere/colors/"
outtt_path = "./_images_/200409_sphere/out/"


layer_count = ut.get_number_of_files(shape_path)
canvas_size = pp.get_size(shape_path + "0000.png")
# print(canvas_size)


for i in range(layer_count):

    number = "%04d"%i
    # print(number)

    shape_name = shape_path + number + ".png"
    ### 0-9 
    color_name = color_path + number[-1] +".png"
    outtt_name = outtt_path + "slice_" + number + ".png"

    color_image = pp.open_img(color_name)
    shape_image = pp.open_img(shape_name)

    # canvas = pp.create_canvas(canvas_size)
    # new_canvas = pp.paste_image(canvas, color_image, (0,0))

    mid = int(layer_count * 0.5)

    canvas = pp.create_canvas(canvas_size)

    if i < mid:
        new_canvas = pp.paste_image(canvas, color_image, (0,0))
    
    elif i >= mid and i < int(layer_count * 0.6):
        new_canvas = pp.paste_image(canvas, color_image, (0, 200))

    elif i >= int(layer_count * 0.7) and i < int(layer_count * 0.8):
        new_canvas = pp.paste_image(canvas, color_image, (0, 200))

    elif i >= int(layer_count * 0.9):
        new_canvas = pp.paste_image(canvas, color_image, (0, 200))

    else:
        new_canvas = pp.paste_image(canvas, color_image, (808, 800))


    new_image = pp.add_shape(new_canvas, shape_image)
    new_image.save(outtt_name, quality=100)

    print("Export : {}".format(i))


print("File_Count : {}".format(layer_count))