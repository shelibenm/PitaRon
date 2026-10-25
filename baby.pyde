

size (256,256)
img = loadImage("face.jpg")
image(img,0,0)
filter (INVERT)
fill(0,220,0)
circle(130,150,5)
save("WTF.jpg")
