class Calc_Color:

    def rgb_to_cmyk(self, rgb):

        # https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
        
        r = float("{0:.8f}".format((rgb[0] / 255.0)))
        g = float("{0:.8f}".format((rgb[1] / 255.0)))
        b = float("{0:.8f}".format((rgb[2] / 255.0)))

        kk = 1.0 - max(r, g ,b)

        if kk == 1.0:
            k = 100
            c = 0
            m = 0
            y = 0

        else:
            k = round(kk * 100)
            c = round(((1.0 - r - kk) / (1.0 - kk)) * 100)
            m = round(((1.0 - g - kk) / (1.0 - kk)) * 100)
            y = round(((1.0 - b - kk) / (1.0 - kk)) * 100)

        return [r, g, b], [c, m, y, k]