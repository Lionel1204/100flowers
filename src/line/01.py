# 01 ~ 03
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower():
  # 01 draw sqare, side=4
  # 02 draw 14 vertices polygon, side=14
  # 03 draw triangle, side=3
  # 19 draw 5 vertices polygon, side=5
  side = 4
  repeat = 10
  for i in range(repeat):
    polygon(500 / side, side)
    right(360 / repeat)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()

run()
getscreen().getcanvas().postscript(file='../../images/01.eps')
hideturtle()
done()
