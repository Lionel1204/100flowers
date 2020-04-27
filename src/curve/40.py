# 39
from turtle import *
from math import *

def arc(radius, angle, direction='left'):
  times = angle // 10
  # every 5 degrees
  perDegree = 5
  for i in range(times):
    if direction == 'right':
      right(perDegree)
    else:
      left(perDegree)

    # sin(10) = 0.1736
    rad = radians(perDegree*2)
    fd(sin(rad) * radius)

    if direction == 'right':
      right(perDegree)
    else:
      left(perDegree)


def leaf(radius, angle):
  times = 2
  for i in range(times):
    arc(radius, angle, 'right')
    right(180 - angle)


def petal():
  left(50)
  radius = 95

  while radius >= 40:
    leaf(radius, 100)
    radius -= 50

  right(50)



def flower():
  times = 12
  for i in range(times):
    pu()
    fd(30)
    pd()
    petal()
    pu()
    fd(-30)
    right(360/times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/40.eps')
done()
