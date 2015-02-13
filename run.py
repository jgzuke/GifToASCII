from PIL import Image
import math
#import numpy
#from matplotlib import pylab
from bisect import bisect
image_file=Image.open("testpng.png")
image_file=image_file.resize((60, 50), Image.ANTIALIAS)
image_file=image_file.convert("L")
weights = ["  ", ".", "-" "/", "*", "%", "#"]
myascii=""
for y in range(0,image_file.size[1]):
    for x in range(0,image_file.size[0]):
        lum=255-image_file.getpixel((x,y))
        myascii+=weights[lum*6/256]
    myascii+="\n"
 
print myascii

#matrix = pylab.imread('testpng.png')
#matrix = numpy.asarray(cv.LoadImageM('testpng.png', 1)).tolist()
#print(matrix)