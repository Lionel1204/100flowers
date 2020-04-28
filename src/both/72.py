# 72
from turtle import *
from src.utils import arc


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower():
  times = 9
  for i in range(times):
    arc(90, 180)
    goto(0, 0)
    left(180)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/72.eps')
done()
