import math
from turtle import *

def hearta(x):
    return 15*math.sin(x)**3

def heartb(x):
    return 12*math.cos(x)-5*\
        math.cos(2*x)-2*\
        math.cos(3*x)-\
        math.cos(4*x)

speed(90000)
bgcolor("black")
for i in range(1000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()
                