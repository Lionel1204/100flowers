# 26

from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def flower():
  times = 12
  for i in range(times):
    angle = 360/times
    fd(70)
    left(angle)
    parallelogram(67, 67, 60)
    right(angle)
    fd(-50)
    right(angle)


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
