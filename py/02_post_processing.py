from operate_color import calc_color, image_processing, util, prepare_print


ut = util.UTIL()
pp = prepare_print.PreparePrint()


outtt_path = "./_images_/200409_sphere/out/"
fix_path = "./_images_/200409_sphere/out_fix/"


layer_count = ut.get_number_of_files(outtt_path)


### export image
for i in range(layer_count):

    number = "%04d"%i
    # print(number)

    outtt_name = outtt_path + "slice_" + number + ".png"
    fix_name = fix_path + "slice_" + number + ".png"

    src_image = pp.open_img(outtt_name)
    changed_image = pp.change_propotion_12(src_image)

    changed_image.save(fix_name, quality=100)

    print("Export : {}".format(i))


### check color
check_name = fix_path + "slice_0300.png"
check_image = pp.open_img(check_name)
check_color = pp.check_color(check_image)

print(check_color)