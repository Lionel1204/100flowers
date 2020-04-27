# 08
from turtle import *


def flower1():
  for i in range(5):
    for i in range(5):
      fd(50)
      right(72)
    right(72)


def flower2():
  for i in range(10):
    for i in range(5):
      fd(110)
      right(72)
    right(36)


def run():
  seth(0)
  goto(0, 0)
  pensize(3)
  pencolor('black')
  speed('fastest')
  pd()
  flower1()
  flower2()


run()
done()
