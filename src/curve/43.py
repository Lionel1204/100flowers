# 43
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


def bird(radius, angle):
  arc(radius, angle, 'right')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'right')
  left(180)


def outline():
  right(10)
  times = 5
  for i in range(times):
    pu()
    fd(130)
    pd()
    bird(30, 150)
    pu()
    goto(0, 0)
    right(360/times)
  left(10)


def flower():
  r = 120
  while r >= 10:
    times1 = 5
    for i in range(times1):
      times2 = 2
      for j in range(times2):
        arc(r, 90, 'right')
        right(360/times2 - 90)

      right(360/times1)

    r-=40


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  outline()


run()
hideturtle()
done()
