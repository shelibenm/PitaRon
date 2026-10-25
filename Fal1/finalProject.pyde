squareSize = 40 
squareX = 30
squareStartY = 70
squareSpeed = 1
blackLineWidth = 10
squareStartX = 30
drawBlackLines = True
def setup(): 
    global blackLineWidth 
    frameRate(15)
    size(640, 360);
    background(240)
    for i in range(0, width / blackLineWidth + 2, 2):
        strokeWeight(blackLineWidth)
        line(i * blackLineWidth, 0, i * blackLineWidth, height)
    

def draw():
    global squareSize,squareX,squareStartY,squareSpeed,blackLineWidth,squareStartX    
    squareX += squareSpeed
    background(240)
    if drawBlackLines == True:
        for i in range(0, width / blackLineWidth + 2, 2):
            stroke(0)
            strokeWeight(blackLineWidth)
            line(i * blackLineWidth, 0, i * blackLineWidth, height)
        
    if squareX > width:
        squareX = squareStartX
    fill(8, 69, 148) #fill square with blue color
    noStroke()
    square(squareX, squareStartY, squareSize)

    fill(255, 211, 45) #fill square with yellow color
    noStroke()
    square(squareX, height - squareStartY - squareSize, squareSize)
    

def mousePressed(): 
    global drawBlackLines
    if drawBlackLines == True:
        drawBlackLines = False
    else:
        drawBlackLines = True
