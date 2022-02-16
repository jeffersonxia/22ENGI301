import time
import random
from bbpystepper import Stepper

step = 35.8
rotation = 45

mod2 = Stepper(pins=["P2_2", "P2_4", "P2_6", "P2_8"])
mod1 = Stepper(pins=["P2_18", "P2_20", "P2_22", "P2_24"])

"""
for i in range(1000):
    for k in range(9):
        mod2.rotate(-step, rotation)
        time.sleep(1)
        print(k)
    for j in range(17):
        mod1.rotate(-2,rotation)            
        mod2.rotate(-2,rotation)
        print(j)

for i in range(1):
    mod2.rotate(random.randint(-360, -9),rotation)
    mod1.rotate(random.randint(-360, -9),rotation)
    time.sleep(1)
"""
    
mod2.zero_angle()
mod1.zero_angle()
"""
    

while(1):
    mod1.rotate(-1,40)
    mod2.rotate(-1,40)
    
    
for j in range(10):
    mod2.rotate(-step , 20)
    time.sleep(0)

while(1):
    i = 0
    if(i%10==0):
        mod1.rotateu

#mod2.rotate(-360)
#mod1.rotate(-360,30)
    
#mod2.rotate(-step*360, 20)

# Rotates motor 180 degrees at 10 RPM
#mystepper.rotate(-3600,60)
#mystepper.angle
#0.0 
"""