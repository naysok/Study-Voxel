function my_color(color) {
    var n = color[0];
    var c_rgb = "rgb(" + color[1] + ", " + color[2] + ", " + color[3] + ")";
    var c_cmyk = color[4] + ", " + color[5] + ", " + color[6] + ", " + color[7];
    return [n, c_rgb, c_cmyk];
}

function flatten(l) {
    for (let k = 0; k < l.length; k++) {
        var tmp = l[k];
        if (k == 0) {
            var a = l[0];
        } else {
            a += l[k];
        }
    }
    return a;
}

var color00 = ["FullCure720", 255, 255, 170, 0, 0, 33, 0];
var color01 = ["Tango", 255, 255, 100, 0, 0, 61, 0];
var color02 = ["TangoBlack", 50, 50, 50, 0, 0, 0, 80];
var color03 = ["Agilus30Clr", 255, 255, 100, 0, 0, 61, 0];
var color04 = ["Agilus30Blk", 40, 77, 108, 63, 29, 0, 58];
var color05 = ["VeroFlexWT", 255, 255, 255, 0, 0, 0, 0];
var color06 = ["VeroPureWht", 240, 240, 240, 0, 0, 0, 0];
var color07 = ["VeroBlack", 26, 26, 29, 10, 10, 0, 89];
var color08 = ["VeroClear", 227, 233, 253, 10, 8, 0, 1];
var color09 = ["VeroCyan", 0, 90, 158, 100, 43, 0, 38];
var color10 = ["VeroMgnt", 166, 33, 98, 0, 80, 41, 35];
var color11 = ["VeroYellow", 200, 189, 3, 0, 5, 99, 22];
var color12 = ["VeroBlue", 156, 208, 237, 34, 12, 0, 7];
var color13 = ["VeroGrey", 185, 185, 185, 0, 0, 0, 27];