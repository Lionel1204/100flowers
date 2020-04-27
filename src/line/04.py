# 04
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower():
  side = 127
  while side > 50:
    for i in range(5):
      polygon(side, 4)
      right(360/5)
    side -= 30


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
