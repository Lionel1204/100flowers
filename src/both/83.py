# 83
from turtle import *
from src.utils import leaf


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def lotus():
  times = 4
  for i in range(times):
    leaf(45, 100, 'right')
    right(120/times)


def leaves():
  for i in range(2):
    leaf(25, 100, 'right')
    left(90)
  left(180)


def flower():
  times = 10
  for i in range(times):
    pu()
    fd(60)

    pd()
    leaves()

    fd(53)
    left(100)

    lotus()
    left(20)

    pu()
    goto(0, 0)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
