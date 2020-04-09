var count = 0;


var old_min = 0.0;
var old_max = 1.0;

var image_path = "out/slice_";


// Slide Bar
var range_0 = document.getElementById('range_0');
var con_text = document.getElementById('con_text');
var con_img = document.getElementById("con_img");

var tmp;
var count;
var count_pad_zero;

var new_min = 0;
var new_max = 2421;





range_0.addEventListener('input', (event) => {

    tmp = range_0.value

    count = parseInt((tmp - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)
    count_pad_zero = ('0000' + count).slice(-4);
    con_text.textContent = "Layer : " + count;
    con_img.src = image_path + count_pad_zero + ".png";

});
// Slide Bar