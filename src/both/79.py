# 79
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
  times = 12
  for i in range(times):
    arc(120, 90, 'right')
    arc(30, 100, 'right')
    goto(0, 0)
    right(170)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
