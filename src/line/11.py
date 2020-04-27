# 11
from turtle import *


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180-angle)


def flower():
  times = 5
  for i in range(times):
    parallelogram(105, 105, 72)
    right(360/times)

  for i in range(times):
    parallelogram(110, 110, 72)
    right(360 / times)

  right(93)
  
  for i in range(times):
    parallelogram(90, 90, 30)
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
