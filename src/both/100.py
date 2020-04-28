# 100
from turtle import *
from src.utils import leaf


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


def leaves(count):
  for i in range(count):
    leaf(40, 80, 'right')
    right(360/count)

def branch():
  fd(30)
  leaf(30, 100, 'right')
  fd(95)
  leaves(7)


def flower():
  times = 10
  for i in range(times):
    branch()
    pu()
    goto(0, 0)
    pd()
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
