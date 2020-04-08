int rad = 200;
int voxel_whd = 400;
float model_height = (25.4 / 300) * voxel_whd; // mm
float layer_height = 0.014; // mm
float current_height = 0;

int end = ceil(model_height / layer_height);
float z_step = float(voxel_whd) / float(end);
int center = int(voxel_whd * 0.5);
int new_rad;
float new_len;
int len_;
int circle_count = 0;


void setup() {
  size(voxel_whd, voxel_whd);
  println("layer count : ", end);
  //  println(z_step);
}

void draw() {

  background(0, 0, 0);
  new_len = Math.abs(center - current_height);
  //  println(current_height);


  if (new_len <= rad) {
    new_rad = 2 * int(sqrt(rad * rad - new_len * new_len));
    fill(255, 255, 255);
    ellipse(center, center, new_rad, new_rad);
    circle_count += 1;
  }


  save("contour/" + nf((frameCount-1), 4) + ".png");
  current_height += z_step;

  if (frameCount == end + 1) {
    println("Circle Count : ", circle_count);
    exit();
  }

  fill(255, 0, 0);
  text(frameCount, center, center);
}

