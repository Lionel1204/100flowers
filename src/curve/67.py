# 67
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


def outerCircle():
  times = 20
  for i in range(times):
    pu()
    fd(120)
    left(90)
    pd()
    arc(30, 360, 'right')
    arc(15, 360, 'right')
    right(90)
    pu()
    goto(0, 0)
    pd()
    right(360/times)


def innerCircle():
  times = 8
  for i in range(times):
    arc(60, 360, 'right')
    right(360/times)


def bigCircle():
  pu()
  goto(-120, 0)
  pd()
  arc(120, 360, 'right')
  pu()
  goto(0, 0)
  pd()


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  bigCircle()
  outerCircle()
  innerCircle()


run()
hideturtle()
done()
