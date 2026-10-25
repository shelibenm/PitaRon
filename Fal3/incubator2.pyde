def setup():
    global img, img1, img2, img3, img4, img5, img6, img7, img8, img9, img11, img12, img13, img14, img15, list1, img22, list2, img33, list3
    img1 = loadImage("deepfryer.png")
    img2 = loadImage("dominos.png")
    img3 = loadImage("kfc.png")
    img4 = loadImage("koreanbbq.png")
    img5 = loadImage("mcdonalds.png")
    img6 = loadImage("microwave.png")
    img7 = loadImage("ramsy.png")
    img8 = loadImage("ricecooker.png")
    img9 = loadImage("SodaPDF-converted-kapanika.png")
    img11 = loadImage("SodaPDF-converted-grill.png")
    img12 = loadImage("forest.png")
    img13 = loadImage("babean.png")
    img14 = loadImage("baby.png")
    img15 = loadImage("SodaPDF-converted-dababy3.png")
    size(340, 340)
    img1.resize(140, 140)
    img2.resize(140, 140)
    img3.resize(140, 140)
    img4.resize(140, 140)
    img5.resize(140, 140)
    img6.resize(140, 140)
    img7.resize(140, 140)
    img8.resize(140, 140)
    img9.resize(140, 140)
    img11.resize(140, 140)
    img12.resize(140, 140)
    img13.resize(140, 140)
    img14.resize(140, 140)
    img15.resize(140, 140)
    list1 = [img1, img6, img4, img8, img11]
    list2 = [img3, img5, img2, img7, img9]
    list3 = [img12, img13, img14, img15]
    img = list1[int(random(5))]
    img22 = list2[int(random(5))]
    img33 = list3[int(random(4))]
def draw():
#    global img1, list1, img22, img33, list2, list3
    image(img, 0, 0)
    image(img22, 200, 0)
    image(img33, 0, 0)
