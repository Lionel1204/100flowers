# 85
from turtle import *
from src.utils import arc, line, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def ring():
  for r in [130, 100]:
    pu()
    goto(-r, 0)
    pd()
    arc(r, 360, 'right')

  pu()
  goto(0, 0)
  pd()


def lines():
  times = 9
  for i in range(times):
    line(100)
    right(360/times)


def flower():
  times = 9
  for r in range(times):
    pu()
    fd(145)
    left(120)
    pd()
    polygon(50, 3)
    right(180)
    polygon(50, 3)
    left(60)
    pu()
    fd(-145)
    right(360 / times)
    pd()


def run():
  init()
  flower()
  lines()
  ring()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/85.eps')
done()
