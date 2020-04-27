# 23

from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def innerPetal():
  right(16)
  parallelogram(55, 55, 30)
  left(16)


def outerPetal():
  right(30)
  polygon(80, 3)
  left(30)


def flower():
  times = 12
  for i in range(times):
    innerPetal()
    pu()
    fd(107)
    pd()
    outerPetal()
    pu()
    goto(0, 0)
    right(360/times)
    pd()



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
