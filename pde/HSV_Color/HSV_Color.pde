void setup() {
  size(100, 50);
  colorMode(HSB, 100);
}
void draw() {
  for (int i=0; i<width; i++) {
    println(i);
    stroke(i,100,100);
    line(i,0, i, height);
  }
  save("result.png");
  exit();
}

