# 30

from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def repeatPolygons(side, vertice, times):
  for i in range(times):
    polygon(side, vertice)
    left(360/times)


def flower(stem):
  times = 8
  for i in range(times):
    pu()
    fd(stem)
    pd()
    fd(70)
    repeatPolygons(28, 3, 4)
    pu()
    goto(0, 0)
    right(360/times)


def diamond():
  times = 8
  for i in range(times):
    pu()
    fd(50)
    pd()
    left(60)
    parallelogram(30, 30, 120)
    right(60)
    pu()
    goto(0, 0)
    right(360/times)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower(80)
  diamond()
  right(22)
  flower(67)



run()
done()
