# 17
from turtle import *

def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def petal():
  size = 47
  pu()
  fd(50)
  pd()
  left(30)
  polygon(size, 3)
  right(30)
  pu()
  fd(44)
  pd()
  left(30)
  polygon(size * 2, 3)
  right(30)


def flower():
  times = 12
  for i in range(times):
    pu()
    goto(0, 0)
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
done()
