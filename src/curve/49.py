# 49
from turtle import *
from math import *


def arcPart(radius, direction='left'):
  # every 5 degrees
  perDegree = 5
  if direction == 'right':
    right(perDegree)
    dot(8)
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


def concentricCircles():
  pensize(5)
  pu()
  goto(0, 0)
  r = 10
  while r <= 80:
    pu()
    goto(r, 0)
    pd()
    arc(r, 360, 'left')
    r += 10


def flower():
  pu()
  times = 20
  for i in range(times):
    fd(130)
    arc(40, 360, 'right')
    goto(0, 0)
    right(360 / times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  concentricCircles()


run()
hideturtle()
done()
