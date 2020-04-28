# 98
from turtle import *
from src.utils import arc, parallelogram


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


def branch():
  groups = 3

  for i in range(groups):
    arc(120, 20, 'right')
    diamondLeaves()

  left(60)


def flower():
  times = 7
  for i in range(times):
    branch()
    pu()
    goto(0, 0)
    pd()
    right(360/times)


def bigCircle():
  r = 175
  pu()
  goto(-r, 0)
  pd()
  arc(r, 360, 'right')


def run():
  init()
  flower()
  bigCircle()


run()
hideturtle()
done()
