from turtle import *
from mpmath import *
import time

shape("turtle")

class beauty:
    def __init__(self, constant, degree, steps):
        self.cons = constant 
        self.deg = degree
        self.steps = steps
        speed(11)
        title(f"{constant} : {degree} degrees : {steps} steps")
        self.constant_dict = {"pi":mp.pi, "degree":mp.degree, "e":mp.e, "phi":mp.phi, "euler":mp.euler, "catalan":mp.catalan} ## apery, khinchin, glaisher, mertens, twin prime

    def draw(self):
        mp.dps = self.steps
        constant = str(self.constant_dict[self.cons]) if self.cons in self.constant_dict else str(mpf(self.cons))
        for i in constant:
            if i != ".":
                forward(5)
                right(int(i)*self.deg)


#penup()
#goto(-300,-300)
#pendown()
#speed(10)
#def spirals(i):
#    forward(5)
#    left(i*1.1)


#for i in range(7200):
#    spirals(i)
func = beauty("phi", 21.114, 10000)
func.draw()

time.sleep(100)


class sierpinski:
    def __init__(self,n):
        triangle = "X"
        replace = {"X":("Y",60,"X",60,"Y"), "Y":("X",-60,"Y",-60,"X")}


        for i in range(n):
            pass

        print(triangle)

def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            fd(length)
            left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        fd(length/2)
        draw_sierpinski(length/2,depth-1)
        bk(length/2)
        left(60)
        fd(length/2)
        right(60)
        draw_sierpinski(length/2,depth-1)


