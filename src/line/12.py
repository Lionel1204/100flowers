# 12
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def petal():
  fd(100)
  left(45)
  polygon(53, 4)
  right(45)
  fd(-100)


def flower():
  times = 12
  for i in range(times):
    petal()
    right(360/times)


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
