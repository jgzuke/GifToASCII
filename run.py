from PIL import Image
import math
#import numpy
#from matplotlib import pylab
from bisect import bisect
image_file=Image.open("test.png")
image_file=image_file.convert("L")
possibilities = " -.'<>=^:+\/*|_%?[]#"

a = [False, False, False]#"000"
b = [True, True, True]#"111"
c = [False, True, False]#"010"
d = [True, False, False]#"100"
e = [False, False, True]#"001"
f = [True, False, True]#"101"
g = [False, True, True]#"011"
h = [True, True, False]#"110"

possibleBools =[[a,a,a,a,a,a,a,a,a],
        [a,a,a,a,b,a,a,a,a],[a,a,a,a,a,a,a,a,b],[b,a,a,a,a,a,a,a,a],
        [a,a,e,c,d,c,e,a,a],[a,a,d,c,e,c,d,a,a],[a,a,a,b,a,b,a,a,a],[c,f,f,a,a,a,a,a,a],[a,a,c,c,a,c,c,a,a],
        [a,a,a,c,b,c,a,a,a],[d,d,d,c,c,c,e,e,e],[e,e,e,c,c,c,d,d,d],[a,a,a,b,b,b,a,a,a],[c,c,c,c,c,c,c,c,c],[a,a,a,a,a,a,a,a,b],
        [h,h,h,b,b,b,g,g,g],[b,b,g,g,c,c,c,c,c],[b,b,d,d,d,d,d,b,b],[b,b,e,e,e,e,e,b,b],
        [b,b,b,b,b,b,b,b,b]]
myascii=""
for j in range((image_file.size[1]/11) - 1):
    for i in range((image_file.size[0]/5) - 1):
        best = possibilities[0]
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
            if matchAmount > largestMatchAmount:
                largestMatchAmount = matchAmount
                best = possibilities[m]
        myascii+=best
    myascii+="\n"
print myascii