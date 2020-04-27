# 10
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower():
  for i in range(12):
    fd(90)
    left(80)
    polygon(85, 3)
    right(80)
    fd(-73)
    right(30)


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
