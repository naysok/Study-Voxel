from operate_color import calc_color, image_processing, util, prepare_print


ut = util.UTIL()
pp = prepare_print.PreparePrint()


in_path = "./_images_/200409_sphere/out_fix/"
alpha_path = "./_images_/200409_sphere/out_alpha/"


layer_count = ut.get_number_of_files(in_path)


### export image
for i in range(layer_count):

    number = "%04d"%i
    # print(number)

    outtt_name = in_path + "slice_" + number + ".png"
    fix_name = alpha_path + "slice_" + number + ".png"

    src_image = pp.open_img(outtt_name)
    changed_image = pp.replace_color_clear(src_image)

    changed_image.save(fix_name, quality=100)

    print("Export : {}".format(i))


### check color
check_name = alpha_path + "slice_0300.png"
check_image = pp.open_img(check_name)
check_color = pp.check_color(check_image)

print(check_color)