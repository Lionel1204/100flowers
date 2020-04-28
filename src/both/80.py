# 80
from turtle import *
from src.utils import leaf, polygon


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
    polygon(125, 4)
    leaf(60, 90, 'right')
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/80.eps')
done()
