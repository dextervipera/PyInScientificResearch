#pidPy

import numpy as np
import matplotlib.pyplot as plt

def SetPiont(t):
    return 0 if t<20 else min(max(t-20,20),150) if t<300 else 0
    
class testobject:
    value = 0
    def deliver(self, val):
        self.value = self.value+max(val,0)
        
    def onestep(self, ambient=20):
        self.value = self.value-(self.value-ambient)*.1

class regulator:
    vp, vi, vd = 0,0,0
    KP, KI, KD = 0.02,0.005,0.1
    lerr = 0
    def onestep(self, sp, tt: testobject, step=.1):
        err = sp - tt.value
        
        self.vd = (err-self.lerr)*self.KD
        self.lerr=err
        
        self.vi = self.vi+self.KI*err
        output = self.KP*err + self.vi + self.vd 
        
        return max(output,0)

plt.axis([-5, 500, -50, 300])

oo = testobject()
rr = regulator()

for t in range(400):

    power = rr.onestep(SetPiont(t),  oo)
    oo.deliver(power)
    
    oo.onestep()
    
    plt.scatter(t, SetPiont(t), c='blue')
    plt.scatter(t,oo.value, c='green')
    plt.scatter(t, power, c='red')
    #plt.pause(0.01)

plt.show()