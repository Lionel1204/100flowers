# 78
from turtle import *
from src.utils import arc, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def bigCircle():
  pu()
  goto(-170, 0)
  pd()
  arc(170, 360, 'right')


def flower():
  times = 12
  for i in range(times):
    fd(80)
    for size in [77, 30]:
      pd()
      left(30)
      polygon(size, 3)
      right(30)
      pu()
      fd(23)

    goto(0, 0)
    pd()
    right(360/times)


def run():
  init()
  flower()
  bigCircle()


run()
hideturtle()
done()
