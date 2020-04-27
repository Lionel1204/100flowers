# 23

from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def petal():
  left(30)
  parallelogram(40, 40, 60)
  fd(40)
  right(60)
  fd(40)
  left(60)
  parallelogram(60, 60, 60)
  right(30)


def flower():
  times = 13
  for i in range(times):
    petal()
    pu()
    goto(0, 0)
    pd()
    right(360/13)


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
