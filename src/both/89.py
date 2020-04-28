# 89
from turtle import *
from src.utils import arc, parallelogram, leaf


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
    pu()

    # half of diamond, goto diamond the opposite angles
    fd(40)
    right(30)
    fd(40)
    right(180 - 30)
    pd()

    #draw a leaf
    left(180)
    arc(30, 150, 'left')
    right(150)
    arc(30, 120, 'right')
    leaf(50, 110, 'left')
    left(120)

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
