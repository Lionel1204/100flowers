# 93
from turtle import *
from src.utils import arc, polygon


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
    polygon(35, 12)
    right(360/times)


def ring():
  times = 45
  for i in range(times):
    pu()
    fd(150)
    pd()
    arc(20, 360, 'right')
    pu()
    goto(0, 0)
    right(360/times)


def run():
  init()
  flower()
  ring()


run()
hideturtle()
done()
