# 55
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


def concentricCircles():
  pu()
  goto(-84, 0)
  pd()
  arc(84, 360, 'right')
  pu()
  goto(-40, 0)
  pd()
  arc(40, 360, 'right')



def flower():
  # 3/5 petals of flower

  times = 10
  for i in range(times):
    pu()
    arc(43, 180, 'right')
    left(180-360/5)

    pd()
    for i in range(3):
      arc(43, 180, 'right')
      left(180-360/5)

    pu()
    arc(43, 180, 'right')
    left(180 - 360 / 5)

    right(360/times)


def run():
  seth(90)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower()
  concentricCircles()


run()
hideturtle()
done()
