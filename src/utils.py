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


def flowerPetal(radius, petalCount):
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
