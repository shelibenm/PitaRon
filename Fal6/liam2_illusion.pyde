
x,y=0,0
def setup(): 
    global hole,stripe,back
    size(200, 200,P2D)   
    hole = createGraphics(40, 40,P2D)
    frameRate(20)
    stripe=loadImage("py.jpg")
    stripe.resize(width,height)
    
    
def draw(): 
    global x,y,stripe,back
    background(120,20,50)
    
   
    holei(x,y)
    #x+=10;y+=10  
    x=int(random(width));y=int(random(height))
    
    copy(stripe,x,y,50,50,x,y,50,50)
 
    
          
def holei(x,y):
    hole.beginDraw()    
    hole.noStroke()    
    hole.ellipseMode(CENTER)    
    hole.circle(20,20,40)
    
    tint(120,120) 
    hole.endDraw()    
    translate(x,y)
    image(hole, x, y)
