# 84
from turtle import *
from src.utils import arc


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def parachute(radius):
  left(30)
  fd(radius * 2)
  right(30)
  arc(radius, 180, 'right')
  right(30)
  fd(radius * 2)
  right(150)

def flower():
  times = 5
  for r in range(25, 75, 10):
    for i in range(times):
      parachute(r)
      right(360 / times)

def run():
  init()
  flower()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/84.eps')
done()
