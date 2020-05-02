# Some basic shapes.

from turtle import *
from math import *


def line(length):
  fd(length)
  fd(-length)


def polygon(size, vertice):
  for i in range(vertice):
    fd(size)
    right(360/vertice)


def parallelogram(side1, side2, angle):
  for i in range(2):
    fd(side1)
    right(angle)
    fd(side2)
    right(180 - angle)


def arcPart(radius, direction='left'):
  # every 5 degrees
  perDegree = 5
  right(perDegree) if direction == 'right' else left(perDegree)

  # sin(10) = 0.1736
  rad = radians(perDegree * 2)
  fd(sin(rad) * radius)

  right(perDegree) if direction == 'right' else left(perDegree)


def arc(radius, angle, direction='left'):
  times = angle // 10
  for i in range(times):
    arcPart(radius, direction)


def leaf(radius, angle, direction='left'):
  for i in range(2):
    arc(radius, angle, direction)
    right(180 - angle) if direction == 'right' else left(180 - angle)


# The vertex should be odd
def asterisk(size, vertex):
  if vertex % 2 == 0:
    raise ValueError('Should input an odd number')

  for i in range(vertex):
    fd(size)
    right(180 - 180 / vertex)


def wintersweet(radius, petalCount):
  for i in range(petalCount):
    arc(radius, 180, 'right')
    left(180 - 360/petalCount)


def bird(radius, angle):
  arc(radius, angle, 'right')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'left')
  left(180)
  arc(radius, angle, 'right')
  left(180)


def parachute(radius):
  left(30)
  fd(radius * 2)
  right(30)
  arc(radius, 180, 'right')
  right(30)
  fd(radius * 2)
  right(150)


def circleWithCenter(x, y, radius):
  pu()
  angle = 0.0
  while angle <= 2 * pi + 0.05:
    goto(radius*cos(angle), radius*sin(angle))
    pd()
    angle += 0.05


def ovalWithCenterAndPoint(x0, y0, x, y):
  pu()
  angle = 0.0
  while angle <= 2 * pi + 0.05:
    goto(x0 + x * cos(angle), y0 + y * sin(angle))
    pd()
    angle += 0.05
