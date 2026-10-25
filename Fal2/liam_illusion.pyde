def setup():
    global img1,xpos,ypos
    size(400,400)
    #frameRate(4)
    
    img1=createImage(200,200,ARGB)    
    img1.loadPixels()
    xpos,ypos = 10,10
    # creating the img with transperent area [small rect]
    for x in range(img1.width): 
     for y in range(img1.height):
        loc= x+y*img1.width
        if x>150 and x<180 and y >150 and y < 180: 
            img1.pixels[loc] = color(100, 0, 0,1)
        else:
            img1.pixels[loc] = color(120,120,200)
    img1.updatePixels()
    
def draw():
    global xpos    
    background(color(xpos,100,xpos)) # you can change the background color to any variable 
    img2=createImage(100,100,RGB)
    fill(color(0,0,20))        
    translate(xpos,ypos)
    image(img1, xpos, ypos)
    xpos+=2
    xpos=constrain(xpos,10,90)
