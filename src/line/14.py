# 14
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def flower():
  r = 133
  for i in range(2):
    times = 20
    for j in range(times):
      parallelogram(50, r, 35)
      left(360/times)
    r -=10


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
