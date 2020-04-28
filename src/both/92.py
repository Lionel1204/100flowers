# 92
from turtle import *
from src.utils import arc, leaf, parallelogram


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
    parallelogram(40, 40, 30)
    # go to the oppsite angle
    fd(40)
    right(30)
    fd(40)
    left(30)

    left(180)
    arc(50, 90, 'right')
    fd(35)
    leaf(45, 110, 'right')
    left(90)
    pu()
    goto(0, 0)
    pd()
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
