#
from matplotlib import pyplot as plt
import math

m = 9.10938356*10**-31 #Mass of electron 
q = -1.602176634*10**-19 # Electric charge
e = 2.5*1000.0 / (0.005*5) # Electric field (v / d) = e
b = 1.38*4.847560976*10**-3*1.0 #Tesla magntic field (f* i) = B

w = b*q/m 
r = e/(b*w) 

def yt(e,m,b,q,r):
    return lambda t :r*(1-math.cos(t*w)) 
def xt(e,m,b,q,r):
    return lambda t: r*(w*t-math.sin(w*t))
def Diffyt(w,r):
    return lambda t :w*r*math.sin(t*w)
def Diffxt(w,r):
    return lambda t :w*r*math.cos(t*w)+r*w
def SecDiffxt(w,r):
    return lambda t :-w**2*r*math.sin(t*w)
def SecDiffyt(w,r):
    return lambda t :w**2*r*math.cos(t*w)

functionforX = xt(e,m,b,q,r)
functionforY = yt(e,m,b,q,r)

#DiffFunctionForX = Diffxt(w,r)
#DiffFunctionForY = Diffyt(w,r)

#SecDiffFunctionForX = SecDiffxt(w,r)
#SecDiffFunctionForY = SecDiffyt(w,r)

PointOfX = list([0.0])
PointOfY = list([0.0])

#DiffPointOfX = list([0.0])
#DiffPointOfY = list([0.0])

#SecDiffPointOfX = list([0.0])
#SecDiffPointOfY = list([0.0])

Sumpoint = 100000
dalta= math.pi*2/(w)/Sumpoint
t = 0.0 #time start
while(-math.pi*2/(w)> t):
    t=t+dalta
    PointOfX.append(functionforX(t))
    PointOfY.append(-functionforY(t))
    #DiffPointOfX.append(DiffFunctionForX(t))
    #DiffPointOfY.append(DiffFunctionForY(t))    
    #SecDiffPointOfX.append(SecDiffFunctionForX(t))
    #SecDiffPointOfY.append(SecDiffFunctionForY(t))

plt.xlabel("x")
plt.ylabel("y")
plt.plot(PointOfX, PointOfY)
#plt.plot(DiffPointOfX, DiffPointOfY)
#plt.plot(SecDiffPointOfX, SecDiffPointOfY)
plt.show()
