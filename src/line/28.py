# 28

from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def flower():
  times = 8
  for i in range(times):
    left(120)
    parallelogram(90, 90, 45)
    fd(90)
    left(30)
    parallelogram(50, 50, 60)
    right(150)
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
