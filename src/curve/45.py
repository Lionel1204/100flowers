# 45
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
  radius = 120
  while radius >= 100:
    for i in range(2):
      arc(radius, 90, 'right')
      right(90)
    radius -= 20


def core():
  right(45)
  pu()
  fd(30)
  left(45)
  pd()
  for i in range(2):
    arc(60, 90, 'right')
    right(90)
  pu()
  goto(0, 0)
  pd()


def flower():
  times = 5
  for i in range(times):
    petal()
    core()
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
