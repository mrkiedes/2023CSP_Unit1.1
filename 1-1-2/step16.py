# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(10)

# move the turtle to another part of the screen
painter.penup()
painter.goto(44, 50)
painter.pendown()

# add code here for an arc
painter.circle(20,50)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-20, -20)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(200,230,5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(47, 7)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(150,360, 9)

# create screen object and make it persists
wn = trtl.Screen()
wn.mainloop()