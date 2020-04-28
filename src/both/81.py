# 81
from turtle import *
from src.utils import arc, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def concentricCircles():
  for r in [80, 30]:
    pu()
    goto(-r, 0)
    pd()
    arc(r, 360, 'right')


def flower():
  times = 10
  for i in range(times):
    pu()
    fd(80)
    left(30)
    pd()
    polygon(112, 3)
    polygon(90, 3)
    pu()
    right(30)
    fd(-80)
    right(360/times)


def run():
  init()
  flower()
  concentricCircles()


run()
hideturtle()
done()
