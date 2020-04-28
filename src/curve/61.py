# 61
from turtle import *
from math import *


def arcPart(radius, direction='left'):
  # every 5 degrees
  perDegree = 5
  right(perDegree) if direction == 'right' else left(perDegree)

  # sin(10) = 0.1736
  rad = radians(perDegree * 2)
  fd(sin(rad) * radius)

  right(perDegree) if direction == 'right' else left(perDegree)


def arc(radius, angle, direction='left'):
  times = angle // 10
  for i in range(times):
    arcPart(radius, direction)


def flower():
  times = 30
  for i in range(times):
    arc(40, 180, 'right')
    arc(50, 180, 'left')
    pu()
    goto(0, 0)
    pd()
    right(360/times)
  pu()
  goto(-180, 0)
  pd()
  arc(180, 360, 'right')


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
getscreen().getcanvas().postscript(file='../../images/61.eps')
done()
