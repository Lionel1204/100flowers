# 37
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
  angle = 100
  for i in range(times):
    arc(85, angle, 'right')
    right(180 - angle)

  for i in range(times):
    arc(85, angle, 'left')
    left(180 - angle)


def flower():
  times = 10
  for i in range(times):
    pu()
    fd(60)
    pd()
    leaf()
    pu()
    goto(0, 0)
    right(360/times)


def flowerHeart():
  pu()
  goto(-30, 0)
  pd()
  arc(30, 360, 'right')
  pu()
  goto(0, 0)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flowerHeart()
  flower()


run()
hideturtle()
done()
