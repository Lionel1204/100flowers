# 51
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


def bird(radius, angle):
  arc(radius, angle, 'right')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'right')
  left(180)



def flower():
  times = 15
  for i in range(times):
    pu()
    fd(25)
    pd()
    bird(30, 110)
    pu()
    fd(38)
    pd()
    bird(70, 110)
    pu()
    goto(0, 0)
    right(360/times)



def heart():
  pu()
  goto(-23, 0)
  pd()
  arc(23, 360, 'right')
  pu()
  goto(0, 0)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  heart()


run()
hideturtle()
done()
