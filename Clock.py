# Made by Emmanuel Abebe
# program discription
# displays a real time clock on screen

import turtle
from math import *
from datetime import datetime
import time

# Screen set up
wn = turtle.Screen()
wn.title("Clock")
wn.bgcolor("gray")
wn.screensize()
wn.setup(width=.9, height=.9, startx=None, starty=None)
wn.tracer(0)

# set up basic properties common to all lines including lines on the clock face and clock hands
class Line(turtle.Turtle):
	def __init__(self,color,length):
		turtle.Turtle.__init__(self)
		self.line = turtle.Turtle()
		self.color(color)
		self.shape("square")
		self.length = length
		self.shapesize(0.1,self.length)
		self.up()

	# moves the hands of the clock in the correct position and angle
	# the clock hands positoned so that 70% of its length is on one side of pivot 
	def run(self,hand):
		self.goto((7*self.length)*cos(hand*pi/180),(7*self.length)*sin(hand*pi/180))
		self.setheading(hand)

	# aligns and posistions the lines on the clock face
	# x_position, y_position positons the line
	# angle sets the line to point towords the center
	# width to determine the thickness of the line
	def label(self,x_position,y_position,angle,width):
		self.goto(x_position,y_position)
		self.shapesize(width,self.length)
		self.setheading(degrees(angle))

# creats objects of line to set up a clock face
class Clockface:
	l = [int(i) for i in range(60)]
	for i in range(60):
		if i%5 == 0: 
			l[i] = Line("black",2).label(300*cos(pi/30*i),300*sin(pi/30*i),pi/30*i,0.3)
		else:
			l[i] = Line("black",0.5).label(300*cos(pi/30*i),300*sin(pi/30*i),pi/30*i,0.1)

# objects for each clock hand
hourhand = Line("black",10)
minutehand = Line("black",15)
secondhand = Line("red",19)

hourhand.shapesize(0.3,10)

class Pivot:
	center = turtle.Turtle()
	center.shape("circle")
	center.shapesize(2)
	center.color("gray")
	center.up()
	center.goto(0,0)

	inner_center = turtle.Turtle()
	inner_center.shape("circle")
	inner_center.shapesize(1)
	inner_center.color("black")
	inner_center.up()
	inner_center.goto(0,0)

class Clock_name:
	pen = turtle.Turtle()
	pen.color("black")
	pen.up()
	pen.ht()
	pen.goto(0,-150)
	pen.write("real_time",align='center',font=("Courier",15,"bold"))

# exception handling for program termination
try:
	while True: 
		wn.update()

		# Uses datetime module to get the real time reading
		# each tick on the clock is 6  
		secondhand.run(90-6*(int(datetime.now().strftime('%S'))))
		minutehand.run(90-6*(int(datetime.now().strftime('%M'))))
		hourhand.run(90-30*(int(datetime.now().strftime('%H'))%12))

	wn.exitonclick()
except Exception as e: pass


