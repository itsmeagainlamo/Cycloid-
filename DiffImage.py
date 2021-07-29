#bring support class
from matplotlib import pyplot as plt
import math
from PIL import Image
import time
from time import sleep
#set info
m = 9.10938356*10**-31 #Mass of electron 
q = -1.602176634*10**-19 # Electric charge
e = 2.5*1000.0 / (0.005*5) # Electric field (v / d) = e
b = 1.38*4.847560976*10**-3*1.0 #Tesla magntic field (f* i) = B
w = b*q/m 
r = e/(b*w)

#load image
PathToRealImage = "a.jpeg"
RealImage= Image.open(PathToRealImage)
pixelmap = RealImage.load()
img = Image.new( RealImage.mode, RealImage.size)
newPixelMap = img.load()
wImage= RealImage.size[0]
hImage= RealImage.size[1]

# Cycloid  Function
def yt(t):
    return  r*(1-math.cos(t*w)) 
def xt(t):
    return  r*(w*t-math.sin(w*t))

#save point
PointOfX = list()
PointOfY = list()

#load point
dalta= -math.pi*2/(w)/100000
t = 0.0 #time start
while(-math.pi*2/(w)> t):
    t=t+dalta
    PointOfX.append(xt(t))
    PointOfY.append(-yt(t))
#set sqre in point

def block(x, y):
    r = 5
    try:
        for i in range(r):
            for j in range(r):
                newPixelMap[y+i, x+j] = (255,255,255)
                newPixelMap[y+i, x-j] = (255,255,255)
                newPixelMap[y-i, x+j] = (255,255,255)
                newPixelMap[y-i, x-j] = (255,255,255)
    except:
        pass

#Main fucntion load
def SeeDeff():
    print("Start")
    print(wImage)
    print(hImage)
    sleep(3)
    for h in reversed(range(hImage)):
        for w in range(wImage):
            newPixelMap[w,h] = pixelmap[w,h]
    print("Finsh load")
    for p in range(len(PointOfX)):
        #print(int(-hImage*PointOfY[p]/(r*2)))
        #print(int(-wImage*PointOfX[p]/(2*math.pi*r)))
        #sleep(0.00005)
        block( int(hImage*PointOfY[p]/(r*2)) ,int(-wImage*PointOfX[p]/(2*math.pi*r)))
    print("Finsh edit")
SeeDeff()
#To see and save the diff
img.save("DiffRelute.jpeg") 
RealImage.close()
img.show() 