# 18
from turtle import *

def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def flower():
  times = 8
  for i in range(times):
    r = 170
    while r > 50:
      polygon(r, 3)
      r -= 40

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
