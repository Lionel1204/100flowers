# 96
from turtle import *
from src.utils import leaf, parachute


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def leaves():
  for r in range(40, 120, 40):
    fd(20)
    left(45)
    leaf(r, 90, 'right')
    pu()
    right(45)
    goto(0, 0)
    pd()


def flower():
  times = 6
  for i in range(times):
    leaves()
    parachute(65)
    right(360/times)


def run():
  init()
  flower()
  leaves()


run()
hideturtle()
done()
