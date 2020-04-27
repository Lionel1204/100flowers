# 34

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


def leaf():
  times = 2
  for i in range(times):
    arc(70, 90, 'right')
    right(90)

  for i in range(times):
    arc(70, 90, 'left')
    left(90)


def flower():
  right(10)
  times = 15
  for i in range(times):
    pu()
    fd(50)
    pd()
    leaf()
    pu()
    goto(0, 0)
    right(360/times)
  left(10)


def ring():
  pu()
  goto(-173, 0)
  pd()
  arc(173, 360, 'right')
  pu()
  goto(-140, 0)
  pd()
  arc(140, 360, 'right')
  pu()
  goto(0, 0)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  ring()
  flower()


run()
hideturtle()
done()
