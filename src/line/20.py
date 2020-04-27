# 20
from turtle import *


def spiral():
  size = 5
  while size <= 50:
    fd(size)
    left(360/5)
    size += 5


def flower():
  times = 12
  for i in range(times):
    pu()
    fd(145)
    pd()
    spiral()
    goto(0, 0)
    pd()
    right(360/times)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
hideturtle()
done()
