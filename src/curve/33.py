# 33

from turtle import *
from math import *

def rightArc(radius, angle):
  times = angle // 10
  # every 5 degrees
  perDegree = 5
  for i in range(times):
    right(perDegree)
    # sin(10) = 0.1736
    rad = radians(perDegree*2)
    fd(sin(rad) * radius)
    right(perDegree)


def leaf():
  rightArc(110, 110)
  right(70)
  rightArc(85, 130)
  right(50)
  pu()
  goto(0, 0)
  pd()

def flower():
  times = 8
  for i in range(times):
    leaf()
    right(360/times)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
hideturtle()
done()
