# 38
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


def petal():
  times = 2
  for i in range(times):
    arc(130, 90, 'right')
    right(90)

  for i in range(times):
    arc(120, 90, 'left')
    left(90)


def flower():
  times = 12
  for i in range(times):
    petal()
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
