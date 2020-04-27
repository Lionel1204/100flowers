# 06
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower():
  times = 6
  for i in range(times):
    polygon(47, 12)
    right(360/times)

  for i in range(times):
    polygon(43, 12)
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
done()
