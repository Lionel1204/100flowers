# 24

from turtle import *


def flower():
  side = 5
  while side <= 130:
    fd(side)
    left(360/9)
    side += 2


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()


run()
done()
