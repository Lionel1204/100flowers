# 99
from turtle import *
from src.utils import leaf, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def diamondLeaves():
  left(60)
  parallelogram(27, 27, 30)
  right(60)
  right(30)
  parallelogram(27, 27, 30)
  left(30)


def lace():
  times = 30
  for i in range(times):
    pu()
    fd(150)
    pd()
    polygon(20, 3)
    left(60)
    polygon(20, 3)
    right(60)
    pu()
    goto(0, 0)
    right(360/times)


def triangles():
  times = 5
  for i in range(times):
    polygon(150, 3)
    right(360/times)


def leaves():
  left(10)
  times = 5
  for i in range(times):
    leaf(100, 80, 'right')
    right(360/times)

  right(10)


def run():
  init()
  leaves()
  triangles()
  lace()


run()
hideturtle()
done()
