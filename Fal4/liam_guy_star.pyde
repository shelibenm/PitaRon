def setup():
  global star
  size(640, 360)

def draw():
  
  background(255)

  fill(0)
  ellipse(width * 0.5, height * 0.5, 200,200)

  fill(255)
  with pushMatrix():
      translate(width * 0.5, height * 0.5)
      rotate(frameCount / 100.0)
      star(0, 0, 50, 200, 8)
      noStroke()

def star(x, y, radius1, radius2, npoints):
  angle = TWO_PI // npoints
  halfAngle = angle * 2
  with beginClosedShape():
      a = 0
      while a < TWO_PI:
          sx = x + cos(a) * radius2
          sy = y + sin(a) * radius2
          vertex(sx, sy)
          sx = x + cos(a + halfAngle) * radius1
          sy = y + sin(a + halfAngle) * radius1
          vertex(sx, sy)
          a += angle
