# 94
from turtle import *
from src.utils import parachute, leaf


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def flower():
  times = 6
  for i in range(times):
    parachute(65)
    left(15)
    leaf(140, 90, 'right')
    right(360/times + 15)


def run():
  init()
  flower()


run()
hideturtle()
done()
