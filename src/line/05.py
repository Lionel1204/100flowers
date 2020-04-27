# 05
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180-angle)


def flower():
  times = 12
  for i in range(times):
    parallelogram(175, 30, 90)
    right(360/times)

  for i in range(times):
    parallelogram(170, 30, 90)
    right(360/times)

  for i in range(times):
    parallelogram(110, 30, 90)
    right(360/times)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
done()
