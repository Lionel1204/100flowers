# 29

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
    parallelogram(20, 20, 30)
    parallelogram(80, 80, 30)
    fd(80)
    left(15)
    parallelogram(50, 50, 30)
    right(15)
    pu()
    goto(0, 0)
    pd()
    left(360/times)


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
