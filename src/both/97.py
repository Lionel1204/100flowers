# 97
from turtle import *
from src.utils import arc, leaf, parachute


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def petal():
  pu()
  fd(55)
  pd()
  leaf(43, 100, 'right')
  fd(120)
  left(80)
  leaf(60, 90, 'left')
  right(80)
  pu()
  goto(0, 0)


def flower():
  times = 12
  for i in range(times):
    petal()
    right(360/times)


def heart():
  r = 20
  pu()
  goto(-r, 0)
  pd()
  arc(r, 360, 'right')


def run():
  init()
  flower()
  heart()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/97.eps')
done()
