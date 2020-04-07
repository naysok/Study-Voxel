def rgb_to_cmyk(rgb):

    cdef int k, c, m, y
    cdef float kk, r, g, b 

    # http://docs.cython.org/en/latest/src/quickstart/build.html
    # https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
        
    r = float("{0:.8f}".format((rgb[0] / 255.0)))
    g = float("{0:.8f}".format((rgb[1] / 255.0)))
    b = float("{0:.8f}".format((rgb[2] / 255.0)))

    kk = 1.0 - max(r, g ,b)

    if kk == 1.0:
        return [r, g, b], [0, 0, 0, 100]

    else:
        k = round(kk * 100)
        c = round(((1.0 - r - kk) / (1.0 - kk)) * 100)
        m = round(((1.0 - g - kk) / (1.0 - kk)) * 100)
        y = round(((1.0 - b - kk) / (1.0 - kk)) * 100)
        
    return [r, g, b], [c, m, y, k]
    

