# 09
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180-angle)


def flower():
  times = 6

  for i in range(times):
    parallelogram(95, 95, 30)
    right(360/times)

  right(30)

  for i in range(times):
    parallelogram(70, 70, 30)
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
hideturtle()
done()
