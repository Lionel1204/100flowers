# 07
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180-angle)


def flower():
  for i in range(8):
    r = 100
    while r > 30:
      parallelogram(r, r, 45)
      r -= 20
    right(45)


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
