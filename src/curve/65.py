# 65
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


def flower():
  times = 10
  for i in range(times):
    arc(40, 180, 'right')
    arc(30, 200, 'left')
    arc(20, 180, 'right')
    leaf(63, 90, 'right')
    left(160)
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
done()
