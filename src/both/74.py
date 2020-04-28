# 74
from turtle import *
from src.utils import line, bird


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower():
  times = 10
  for i in range(times):
    pu()
    fd(65)
    pd()
    bird(70, 110)
    pu()
    goto(0, 0)
    right(360/times)


def heart():
  times = 10
  for i in range(times):
    line(80)
    right(360/times)


def run():
  init()
  heart()
  flower()


run()
hideturtle()
done()
