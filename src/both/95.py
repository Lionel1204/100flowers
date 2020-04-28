# 95
from turtle import *
from src.utils import arc, parallelogram, line


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def diamonds():
  times = 10
  angle = 45
  for i in range(times):
    for r in range(40, 10, -10):
      parallelogram(r, r, angle)
      fd(r)
      right(angle)
      fd(r)
      left(angle)
    pu()
    goto(0, 0)
    pd()

    right(360/times)


def spokes():
  right(5)
  times = 10
  for i in range(times):
    line(170)
    right(360/times)

  left(5)

def ring():
  for r in [170, 180]:
    pu()
    goto(-r, 0)
    pd()
    arc(r, 360, 'right')

def run():
  init()
  diamonds()
  spokes()
  ring()


run()
hideturtle()
done()
