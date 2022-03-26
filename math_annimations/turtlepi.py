from turtle import *
from mpmath import mp
import time

shape("turtle")

class beauty:
    def __init__(self, constant, degree, steps):
        self.cons = constant 
        self.deg = degree
        self.steps = steps
        speed(10)
        title(f"{constant} : {degree} degrees : {steps} steps")
        self.constant_dict = {"pi":mp.pi, "degree":mp.degree, "e":mp.e, "phi":mp.phi, "euler":mp.euler, "catalan":mp.catalan} ## apery, khinchin, glaisher, mertens, twin prime

    def draw(self):
        mp.dps = self.steps
        constant = str(self.constant_dict[self.cons])
        for i in constant:
            if i != ".":
                forward(10)
                right(int(i)*self.deg)


#penup()
#goto(-300,-300)
#pendown()
speed(10)
def spirals(i):
    forward(5)
    left(i*1.1)


for i in range(7200):
    spirals(i)
#func = beauty("e", 90, 1000)
#func.draw()

time.sleep(100)

