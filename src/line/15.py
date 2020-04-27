# 15
from turtle import *


def flower():
  times1 = 12
  for i in range(times1):
    fd(100)

    times2 = 7
    for j in range(times2):
      fd(85)
      right(180 - 180 / times2)

    fd(-80)
    right(360/times1)


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
