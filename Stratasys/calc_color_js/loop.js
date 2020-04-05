var txt = [];
for (let i = 0; i < 14; i++) {
    number = ('0' + i).slice(-2);
    txt.push(
        "var t_" + number + " = document.getElementById(\"text_" + number + "\");" +
        "var b_" + number + " = document.getElementById(\"box_" + number + "\");" +
        "var tmp = my_color(color" + number + ");" +
        "t_" + number + ".textContent = \"Material Name : \" + tmp[0] + \" / CMYK : \" + tmp[2];\n" +
        "b_" + number + ".style.background = tmp[1];"

    );
}

var dev = document.getElementById("devMsg");
dev.textContent = flatten(txt);