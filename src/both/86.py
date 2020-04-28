# 86
from turtle import *
from src.utils import arc, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def outer():
  times = 5
  for i in range(times):
    polygon(38, 4)
    right(360/times)


def flower():
  times = 8
  for i in range(times):
    pu()
    fd(130)
    pd()
    outer()
    pu()
    fd(-130)
    right(360/times)


def heart():
  pu()
  goto(-30, 0)
  pd()
  arc(30, 360, 'right')


def run():
  init()
  flower()
  heart()


run()
hideturtle()
done()
