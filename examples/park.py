import turtle
import random

turtle.shape('turtle')
turtle.speed('fastest')

def polynomial(n):
  for i in range(n):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    turtle.color(red, green, blue)
    turtle.forward(10)
    turtle.left(360/n)
    
for i in range(3, 100):
  polynomial(i)



# NE

import turtle
import random

turtle.shape('turtle')
turtle.speed('fastest')
turtle.width(3)

def teleport():
  x = random.randint(-190, 190)
  y = random.randint(-190, 190)
  turtle.goto(x, y)
  
def set_random_color():
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)
  turtle.color(red, green, blue)
  
def is_lost():
  return abs(turtle.xcor()) > 190 or abs(turtle.ycor()) > 210

while True:
  set_random_color()
  turtle.left(random.randint(0, 360))
  turtle.forward(100)
  if is_lost():
    teleport()