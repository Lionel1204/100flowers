# 54
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


def littleFlower():
  times = 6
  for i in range(times):
    for j in range(2):
      arc(30, 70, 'right')
      right(110)

    right(360/times)


def petal(size):
  left(60)
  for i in range(2):
    arc(size, 120, 'right')
    right(60)
  right(60)


def flower():
  times = 14
  for i in range(times):
    pu()
    fd(30)
    pd()
    petal(80)
    pu()
    fd(-30)
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
