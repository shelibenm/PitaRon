def setup():
   
    global img, img1, img2, img3, img4, img5, img6, img7, img8, img9, img11,img12, img13, img14, img15, list1, img22, list2, img33, list3
    size(340, 340)
    img1 = loadImage("deepfryer.png")
    img2 = loadImage("dominos.png")
    img3 = loadImage("kfc.png")
    img4 = loadImage("koreanbbq.jpg")
    img5 = loadImage("mcdonalds.jpg")
    img6 = loadImage("microwave.jpg")
    img7 = loadImage("ramsy.png")
    img8 = loadImage("ricecooker.png")
    img9 = loadImage("kapanika.png")
    img11 = loadImage("grill.png")
    img12 = loadImage("forest.png")
    img13 = loadImage("babean.png")
    img14 = loadImage("baby.png")
    img15 = loadImage("dababy.png")
     
    list1 = [img1, img6, img4, img8, img11]
    list2 = [img3, img5, img2, img7, img9]
    list3 = [img12, img13, img14, img15]
    
def draw():
        global img33
        if mousePressed:
            img =   list1[int(random(5))]
            img22 = list2[int(random(5))]
            img33 = list3[int(random(4))]
            
            image(img,0, 0,140,140)                  
            image(img22, 200, 0,140,140)
            
        if keyPressed:
            if key == 'a':    
                image(img33, 100, 200,140,140)
            else: 
                rect(100,200,140,140)
