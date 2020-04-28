# 75
from turtle import *
from src.utils import leaf


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def petal():
  for r in range(60, 100+1, 20):
    leaf(r, 90, 'right')


def flower():
  times = 10
  for i in range(times):
    fd(50)
    petal()
    goto(0, 0)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/75.eps')
done()
