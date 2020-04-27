# 46
from turtle import *
from math import *


def arcPart(radius, direction='left'):
  # every 5 degrees
  perDegree = 5
  if direction == 'right':
    right(perDegree)
  else:
    left(perDegree)

  # sin(10) = 0.1736
  rad = radians(perDegree * 2)
  fd(sin(rad) * radius)

  if direction == 'right':
    right(perDegree)
  else:
    left(perDegree)


def arc(radius, angle, direction='left'):
  times = angle // 10
  for i in range(times):
    arcPart(radius, direction)


def twoLeaves():
  for i in range(2):

    for j in range(2):
      arc(15, 90, 'right')
      right(90)

    left(90)

  left(360/2)


def branch():
 times = 5
 for i in range(times):
   leavesCount = 12
   for j in range(leavesCount):
     arcPart(90, 'right')
     twoLeaves()

   left(120)
   pu()
   goto(0, 0)
   right(360/times)
   pd()


def flower():
  times = 5
  for i in range(times):
    for j in range(2):
      arc(90, 120, 'right')
      right(60)

    right(360 / times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  branch()


run()
hideturtle()
done()
