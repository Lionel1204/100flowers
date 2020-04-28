# 57
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


def leaf(radius, angle):
  for i in range(2):
    arc(radius, angle, 'right')
    right(180-angle)


def branch():
  r = 20
  # 3 groups leaves
  for i in range(3):
    arc(80, 30, 'right')
    left(90)
    for j in range(2):
      leaf(r, 90)
      right(180 - 90)

    left(90)
    r += 7
  left(90)


def flower():
  times = 7
  for i in range(times):
    branch()
    pu()
    goto(0, 0)
    right(360/times)
    pd()


def bigCircle():
  size = 177
  while size >= 167:
    pu()
    goto(-size, 0)
    pd()
    arc(size, 360, 'right')
    size -= 10


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  bigCircle()


run()
hideturtle()
done()
