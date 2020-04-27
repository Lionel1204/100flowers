# 50
from turtle import *
from math import *


def arcPart(radius, direction='left'):
  # every 5 degrees
  perDegree = 5
  if direction == 'right':
    right(perDegree)
  else:
    left(perDegree)

  # sin(10) = 0.1736
  rad = radians(perDegree * 2)
  fd(sin(rad) * radius)

  if direction == 'right':
    right(perDegree)
  else:
    left(perDegree)



def arc(radius, angle, direction='left'):
  times = angle // 10
  for i in range(times):
    arcPart(radius, direction)


def petal():
  arc(40, 120, 'right')
  arc(80, 60, 'left')
  arc(30, 80, 'right')
  left(140)
  arc(85, 162, 'left')
  right(160)


def flower():
  times = 12
  for i in range(times):
    petal()
    pu()
    goto(0, 0)
    right(360 / times)
    pd()


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
#getscreen().getcanvas().postscript(file='../../images/50.eps')
done()
