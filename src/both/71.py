# 71
from turtle import *
from src.utils import arc


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower2():
  times = 6
  for i in range(times):
    fd(153)
    pu()
    goto(0, 0)
    right(360/6)
    pd()


def flower1():
  times = 6
  for i in range(times):
    arc(90, 360, 'right')
    right(360/times)


def run():
  init()
  flower1()
  flower2()


run()
hideturtle()
done()
