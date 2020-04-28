# 69
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


def core():
  right(45)
  pu()
  fd(60)
  left(45)
  pd()
  leaf(60, 90, 'right')
  pu()
  goto(0, 0)
  pd()


def petal():
  leaf(130, 90, 'right')


def flower():
  times = 10
  for i in range(times):
    petal()
    core()
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
getscreen().getcanvas().postscript(file='../../images/69.eps')
done()
