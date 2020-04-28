# 73
from turtle import *
from src.utils import leaf


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def leaves(count):
  times = 10
  for i in range(times):
    pu()
    fd(120)
    left(90)
    pd()
    for i in range(count):
      left(10)
      leaf(45, 80, 'right')
      right(10)
      right(180/count)
    left(90)
    pu()
    goto(0, 0)
    right(360/times)


def stem():
  times = 10
  for i in range(times):
    fd(120)
    fd(-120)
    right(360/times)


def run():
  init()
  stem()
  leaves(3)


run()
hideturtle()
done()
