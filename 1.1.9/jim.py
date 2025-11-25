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
jim.setheading(0)
jim.forward(50)
jim.left(90)
jim.forward(100)
jim.left(180)
jim.pendown()

'''if jim.pencolor("pink"):
    jim.pencolor("black")
elif jim.pencolor("black"):
    jim.pencolor("blue")
else:
    jim.pencolor("red")'''
for head in range(6):
    jim.circle(100,180)
    jim.right(120)

jim.teleport(0,-150)
jim.setheading(0)
jim.setheading(270)
jim.forward(50)
jim.right(90)
jim.forward(20)
jim.left(90)
jim.forward(10)
jim.left(90)
jim.forward(30)
jim.left(90)
jim.forward(50)
jim.penup()
jim.teleport(0,0)
jim.setheading(0)
jim.forward(300)
jim.right(90)
jim.forward(150)
jim.pendown()
jim.forward(50)
jim.left(90)
jim.forward(20)
jim.right(90)
jim.forward(10)
jim.right(90)
jim.forward(30)
jim.right(90)
jim.forward(50)

jim.setheading(0)
jim.teleport(0,0)
jim.pencolor("black")
for tut in range(2):
    jim.forward(300)
    jim.right(90)
    jim.forward(150)
    jim.right(90)









wn = trtl.Screen()
wn.mainloop()