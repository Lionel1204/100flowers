# 01 ~ 03
from turtle import *


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  repeat = 10
  for i in range(repeat):
    # 01 draw sqare
    polygon(500/4, 4)

    # 02 draw 14 vertices polygon
    #polygon(500/14, 14)

    # 03 draw triangle
    #polygon(500/3, 3)

    right(360/repeat)

run()
done()
