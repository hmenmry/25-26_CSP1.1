# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
leg_number = 8
leg_length = 72
leg_spacing = 380 / leg_number
spider.pensize(5)
inc = 0

#DRAW LEGS
while inc < leg_number:
  spider.goto(0, 0)
  spider.setheading(leg_spacing * inc)
  spider.forward(leg_length)
  inc = inc + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()