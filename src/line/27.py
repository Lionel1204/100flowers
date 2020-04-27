# 27

from turtle import *


def flower():
  times = 10
  angle = 360/times
  for i in range(times):
    for j in range(8):
      fd(55)
      right(angle)

    right(2 * angle)
    pu()
    goto(0, 0)
    pd()
    right(angle)



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
