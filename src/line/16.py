# 16
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def lace():
  times = 20
  for i in range(times):
    pu()
    fd(147)
    pd()
    polygon(30, 3)
    fd(30)
    polygon(-30, 3)
    fd(-30)
    pu()
    goto(0, 0)
    right(360/times)
    pd()


def petal():
  times = 10
  for i in range(times):
    fd(100)
    polygon(50, 3)
    fd(50)
    polygon(-50, 3)
    fd(-50)
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
  petal()
  lace()


run()
done()
