# 21
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def diamond():
  pu()
  fd(105)
  pd()
  right(60)
  fd(105)
  right(180-60)
  fd(105)
  pu()
  right(60)
  fd(105)
  right(180-60)
  pd()


def flower():
  left(15)
  times = 12
  for i in range(times):
    diamond()
    right(30)

  for i in range(times):
    parallelogram(67, 67, 30)
    right(30)


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
