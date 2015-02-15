from PIL import Image
import math
import random
from bisect import bisect

weights = [" ", ".'", ".-'", "_-^", "%?[]\/*", "#", "#", "#", "#", "#", "#"]
a = [False, False, False]#"000"
b = [True, True, True]#"111"
c = [False, True, False]#"010"
d = [True, False, False]#"100"
e = [False, False, True]#"001"
f = [True, False, True]#"101"
g = [False, True, True]#"011"
h = [True, True, False]#"110"
bools =[[],
        [[a,a,a,a,a,a,a,a,b],[b,a,a,a,a,a,a,a,a]],
        [[a,a,a,a,a,a,a,a,b],[a,a,a,a,b,a,a,a,a],[b,a,a,a,a,a,a,a,a]],
        [[a,a,a,a,a,a,a,a,b],[a,a,a,a,b,a,a,a,a],[c,f,f,a,a,a,a,a,a]],
        [[h,h,h,b,b,b,g,g,g],[b,b,g,g,c,c,c,c,c],[b,b,d,d,d,d,d,b,b],[b,b,e,e,e,e,e,b,b],[d,d,d,c,c,c,e,e,e],[e,e,e,c,c,c,d,d,d],[a,a,a,b,b,b,a,a,a]],
        [],
        [],
        [],
        [],
        [],
        []]

def resize(image, lines):
    lines *= 10
    wpercent = (lines/float(image.size[1]))
    hsize = int((float(image.size[0])*float(wpercent)))
    return image.resize((hsize,lines), Image.ANTIALIAS)

def removeAlpha(image):
    image.load()  # needed for split()
    image.convert("RGBA")
    if image.mode == "RGBA":
        background = Image.new('RGB', image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
        return background.convert("L")
    else:
        return image.convert("L")

def addContrast(image, lighten, contrast):
    image = image.point(lambda p: p + lighten) 
    return image.point(lambda p: ((p-128)*contrast)+128)

def getImage(name, lines, lighten, contrast):
    image = Image.open(name)
    image = resize(image, lines)
    image = removeAlpha(image)
    image = addContrast(image, lighten, contrast)
    return image

def getASCII(name, lines=40, lighten=0, contrast=2):
    image = getImage(name, lines, lighten, contrast)
    myascii="\n"
    for j in range((image.size[1]/10)):
        for i in range((image.size[0]/5)):
            weight = 0
            for y in range(9):
                for x in range(5):
                    lum=255-image.getpixel((x+(5*i),y+(10*j)))
                    weight += lum
            weight /= 50
            index = weight*6/256
            possibilities = weights[index]
            possibleBools = bools[index]

            best = ""
            if len(possibilities) == 1:
                myascii+=possibilities[0]
            else:
                largestMatchAmount = 0
                for m in range(len(possibilities)):
                    letter = possibleBools[m]
                    matchAmount = 0
                    for y in range(1,9):
                        for x in range(1,4):
                            if letter[y-1][x-1]:
                                lum=255-image.getpixel((x+(5*i),y+(10*j)))
                                matchAmount += lum
                            else:
                                lum=image.getpixel((x+(5*i),y+(10*j)))
                                matchAmount += lum
                    if matchAmount >= largestMatchAmount:
                        largestMatchAmount = matchAmount
                        best += possibilities[m]
                char = best[random.randint(0, len(best)-1)]
                myascii+=char
        myascii+="\n"
    myascii+="\n"
    return myascii


#print getASCII("adam.jpg", 1600, 0, 2)
print getASCII("stickman.png", 19, 70, 2)
#print getASCII("icon.png", 400, 0.6, 6)
#print getASCII("displaypic.png", 400, 1, 1)
#print getASCII("test.png", 400, 1, 1)
#print getASCII("favicon.ico", 400, 1, 1)

#print getASCII("icon.png", 800)