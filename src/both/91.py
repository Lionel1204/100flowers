# 90
from turtle import *
from src.utils import arc, leaf, parallelogram


def init():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()


def ring():
  for r in [20, 40]:
    pu()
    goto(-r, 0)
    pd()
    arc(r, 360, 'right')

  pu()
  goto(0, 0)


def leaves():
  seth(0)
  times = 10
  for i in range(times):
    pu()
    fd(40)
    pd()
    leaf(70, 50, 'right')
    leaf(70, 50, 'left')
    pu()
    goto(0, 0)
    right(360/times)


def diamonds():
  angle = 45
  for l in [100, 70]:
    times = 10
    for i in range(times):
      pu()
      fd(l)
      pd()
      left(angle/2)
      parallelogram(40, 40, angle)
      pu()
      goto(0, 0)
      right(angle/2)

      right(360/times)


def run():
  init()
  ring()
  leaves()
  diamonds()


run()
hideturtle()
getscreen().getcanvas().postscript(file='../../images/91.eps')
done()
