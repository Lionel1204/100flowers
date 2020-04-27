# 35
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
    rad = radians(perDegree * 2)
    fd(sin(rad) * radius)

    if direction == 'right':
      right(perDegree)
    else:
      left(perDegree)


def flower():
  times = 10
  for i in range(10):
    arc(20, 180, 'right')
    left(180)
    arc(50, 180, 'right')
    left(180)
    arc(20, 180, 'right')
    arc(90, 180, 'right')
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
