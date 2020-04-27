# 31
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


def flower():
  times = 8
  for i in range(times):
    rightArc(85, 360)
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
