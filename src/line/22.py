# 22
from turtle import *

def petal(side, times):
  # 7+3+2 = times
  for i in range(7):
    fd(side)
    right(360/times)

  pu()
  for i in range(3):
    fd(side)
    right(360/times)

  pd()
  for i in range(2):
    fd(side)
    right(360/times)

def flower():
  times = 12
  side = 47
  for i in range(times):
    petal(side, times)
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
