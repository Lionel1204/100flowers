# 87
from turtle import *
from src.utils import arc, leaf, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower():
  times = 8
  for i in range(times):
    polygon(160, 3)
    right(360/times)


def ring():
  for r in [160, 180]:
    pu()
    goto(-r, 0)
    pd()
    arc(r, 360, 'right')


def run():
  init()
  flower()
  ring()


run()
hideturtle()
done()
