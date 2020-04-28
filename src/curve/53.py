# 53
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


def petal():
  arc(90, 110, 'right')
  littleFlower()
  right(70)
  arc(80, 110, 'right')
  right(70)
  pu()
  goto(0, 0)
  pd()


def flower():
  times = 8
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
