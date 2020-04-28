# 52
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


def leaf():
  left(10)
  for i in range(2):
    arc(40, 80, 'right')
    right(180 - 80)
  right(10)


def leaves(count):
  for i in range(count):
    leaf()
    right(180/count)


def flowerOuter():
  times = 10
  for i in range(times):
    pu()
    fd(120)
    left(90)
    pd()
    leaves(3)
    left(90)
    pu()
    goto(0, 0)
    right(360/times)



def flowerInner():
  times = 10
  for i in range(times):
    arc(60, 360, 'right')
    right(360/times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flowerInner()
  flowerOuter()


run()
hideturtle()
done()
