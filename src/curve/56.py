# 56
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


def flower():
  times = 12
  for i in range(times):
    arc(90, 150, 'right')
    right(90)
    arc(65, 155, 'right')
    right(90)
    left(120)
    pu()
    goto(0, 0)
    pd()
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
getscreen().getcanvas().postscript(file='../../images/56.eps')
done()
