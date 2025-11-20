import turtle as trtl


jim = trtl.Turtle()


# rectangle body
for tut in range(2):
    jim.forward(300)
    jim.right(90)
    jim.forward(150)
    jim.right(90)

jim.color("purple")
jim.pensize(25)
jim.left(120)
jim.circle(50, 180)
jim.left(180)
jim.circle(50, -180)
jim.penup()
jim.teleport(300, 0)
jim.pendown()
jim.circle(50, -180)
jim.left(180)
jim.circle(50, 180)
jim.color("violet")
jim.penup()
jim.teleport(0,0)

wn = trtl.Screen()
wn.mainloop()