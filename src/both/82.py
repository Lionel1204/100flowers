# 82
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
  times = 3
  for i in range(times):
    leaf(85, 90, 'right')
    right(100/times)


def flower():
  times = 6
  for i in range(times):
    fd(55)
    left(80)
    lotus()
    left(20)
    goto(0, 0)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
