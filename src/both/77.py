# 77
from turtle import *
from src.utils import leaf, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def fan():
  times = 6
  for i in range(times):
    polygon(50, 3)
    right(120/times)

def fans():
  times = 5
  for i in range(times):
    right(20)
    pu()
    fd(130)
    pd()
    left(70)
    fan()
    left(70)
    pu()
    goto(0, 0)
    right(360/times)



def flower():
  times = 5
  for i in range(times):
    leaf(100, 120, 'right')
    right(360/times)


def run():
  init()
  flower()
  fans()


run()
hideturtle()
done()
