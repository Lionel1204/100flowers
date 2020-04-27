# 32
from turtle import *
from math import *

def rightCircle(radius):
  times = 36
  # every 5 degrees
  perDegree = 5
  for i in range(times):
    right(perDegree)
    # sin(10) = 0.1736
    rad = radians(perDegree*2)
    fd(sin(rad) * radius)
    right(perDegree)


def flower():
  r = 95
  while r >= 70:
    times = 6
    for i in range(times):
      rightCircle(r)
      right(360/times)
    r -= 10


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
hideturtle()
done()
