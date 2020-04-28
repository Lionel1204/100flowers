# 76
from turtle import *
from src.utils import flowerPetal, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower2():
  times = 20
  for i in range(times):
    pu()
    fd(160)
    pd()
    flowerPetal(10, 5)
    pu()
    goto(0, 0)
    pd()
    right(360/times)


def flower1():
  times = 8
  for i in range(times):
    polygon(120, 3)
    right(360/times)


def run():
  init()
  flower1()
  flower2()


run()
hideturtle()
done()
