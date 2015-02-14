from PIL import Image
import math
import random
from bisect import bisect

weights = [" ", ".'", ".-'", "_-^", "%?[]\/*", "#", "#", "#"]
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
        []]

def getImage(name, size):

    image_file = Image.open(name)
    wpercent = (size/float(image_file.size[0]))
    hsize = int((float(image_file.size[1])*float(wpercent)))
    image_file = image_file.resize((size,hsize), Image.ANTIALIAS)

    image_file.convert("RGBA")
    pixel_data = image_file.load()
    if image_file.mode == "RGBA":
        for y in xrange(image_file.size[1]):
            for x in xrange(image_file.size[0]):
                if pixel_data[x, y][3] < 255:
                    pixel_data[x, y] = (255, 255, 255, 255)
    image_file=image_file.convert("L")
    return image_file

def getASCII(name, size):
    image_file = getImage(name, size)
    myascii="\n\n"
    for j in range((image_file.size[1]/11)):
        for i in range((image_file.size[0]/5)):
            weight = 0
            for y in range(11):
                for x in range(5):
                    lum=255-image_file.getpixel((x+(5*i),y+(11*j)))
                    weight += lum
            weight /= 45
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
                    for y in range(1,10):
                        for x in range(1,4):
                            if letter[y-1][x-1]:
                                lum=255-image_file.getpixel((x+(5*i),y+(11*j)))
                                matchAmount += lum
                            else:
                                lum=image_file.getpixel((x+(5*i),y+(11*j)))
                                matchAmount += lum
                    if matchAmount >= largestMatchAmount:
                        largestMatchAmount = matchAmount
                        best += possibilities[m]
                char = best[random.randint(0, len(best)-1)]
                myascii+=char
        myascii+="\n"
    myascii+="\n\n"
    return myascii



print getASCII("test.png", 800)
print getASCII("testpng.png", 800)
print getASCII("icon.png", 800)