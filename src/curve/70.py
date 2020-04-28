# 70
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


def leaf(radius, angle, direction='left'):
  for i in range(2):
    arc(radius, angle, direction)
    right(180 - angle) if direction == 'right' else left(180 - angle)


def lotus():
  times = 5
  for i in range(times):
    leaf(30, 100, 'right')
    right(170/times)


def branch():
  times = 3
  for i in range(times):
    arcPart(100, 'right')
    leaf(20, 100, 'right')
    arcPart(100, 'right')
    leaf(20, 100, 'left')

  arc(100, 20, 'right')
  left(110)
  lotus()

  pu()
  goto(0, 0)
  left(140)
  pd()


def flower():
  times = 7
  for i in range(times):
    branch()
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
getscreen().getcanvas().postscript(file='../../images/70.eps')
done()
