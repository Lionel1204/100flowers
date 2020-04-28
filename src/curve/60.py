# 60
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


def bird(radius, angle):
  arc(radius, angle, 'right')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'right')
  left(180)


def leaf(radius, angle, direction = 'left'):
  for i in range(2):
    arc(radius, angle, direction)
    right(180 - angle) if direction == 'right' else left(180 - angle)


def birds():
  times = 7
  for i in range(times):
    pu()
    fd(100)
    pd()
    bird(60, 90)
    pu()
    goto(0, 0)
    right(360/times)

def flower():
  times = 7
  for i in range(times):
    r = 210
    while r >= 70:
      leaf(r, 50, 'right')
      r -= 50
    right(360/7)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  birds()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/60.eps')
done()
