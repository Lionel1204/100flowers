# 08
from turtle import *

def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower1():
  times = 5
  for i in range(times):
    polygon(50, 5)
    right(360/times)


def flower2():
  times = 10
  for i in range(times):
    polygon(110, 5)
    right(360/times)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower1()
  flower2()


run()
hideturtle()
done()
