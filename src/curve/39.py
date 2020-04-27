# 39
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
  pu()
  arc(100, 30, 'right')
  pd()
  arc(100, 90, 'right')
  right(60)
  arc(100, 90, 'right')
  pu()
  arc(100, 30, 'right')
  right(60)


def flower():
  times = 8
  for i in range(times):
    petal()
    right(360/times)


def flowerHeart():
  pu()
  goto(-20, 0)
  pd()
  arc(20, 360, 'right')
  pu()
  goto(-50, 0)
  pd()
  arc(50, 360, 'right')
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
