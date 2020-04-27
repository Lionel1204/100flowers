# 42
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


def curvedSquare():
  for i in range(4):
    arc(50, 90, 'right')
    left(90)
    arc(50, 90, 'left')


def twiningFlower():
  times = 10
  for i in range(times):
    curvedSquare()
    right(360/times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  twiningFlower()


run()
hideturtle()
done()
