#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:

for maze in range(2):
  for turns in range(3):
    turn_left()
  move()
  turn_left()
  for fwd in range(2):
    move()
  for turns in range(3):
    turn_left()
  move()
  turn_left()
  robot.pencolor("blue")
'''
for step in range(2): # repeat 2 times
  move()    # forward 1
  for turn in range(3): # turn right
    turn_left()
  for step in range(2): # forward 2
    move()
  turn_left()   # turn left
  move()        # forward 1
  robot.pencolor("blue")
'''

#---- end robot movement 

wn.mainloop()
