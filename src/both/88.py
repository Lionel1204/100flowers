# 88
from turtle import *
from src.utils import arc, leaf, polygon


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def parachute(radius):
  left(30)
  fd(radius * 2)
  right(30)
  arc(radius, 180, 'right')
  right(30)
  fd(radius * 2)
  right(150)


def flower():
  times = 6
  for i in range(times):
    parachute(50)
    fd(20)
    left(45)
    leaf(50, 90, 'right')
    pu()
    right(45)
    goto(0, 0)
    pd()
    right(360/times)


def hexagon():
  times = 6
  for i in range(times):
    polygon(180, 3)
    polygon(170, 3)
    right(360/times)


def run():
  init()
  hexagon()
  flower()


run()
hideturtle()
done()
