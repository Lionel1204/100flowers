# 90
from turtle import *
from src.utils import parachute


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
    parachute(65)
    right(360/times)


def run():
  init()
  flower()


run()
hideturtle()
done()
