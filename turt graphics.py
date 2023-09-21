import random
import turtle

# function to check whether turtle
# is in Screen or not
def isInScreen(win, turt):
	
	# getting the end points of turtle screen
	leftBound = -win.window_width() / 2
	rightBound = win.window_width() / 2
	topBound = win.window_height() / 2
	bottomBound = -win.window_height() / 2

	# getting the current position of the turtle
	turtleX = turt.xcor()
	turtleY = turt.ycor()

	# variable to store whether in screen or not
	stillIn = True

	# condition to check whether in screen or not
	if turtleX > rightBound or turtleX < leftBound:
		stillIn = False
	if turtleY > topBound or turtleY < bottomBound:
		stillIn = False

	# returning the result
	return stillIn


# function to check whether both turtle have
# different position or not
def sameposition(Cerulean, Purple):
	if Cerulean.pos() == Purple.pos():
		return False
	else:
		return True

# main function
def main():

	# screen initialization for turtle
	wn = turtle.Screen()

	# Turtle Cerulean initialization
	# instantiate a new turtle object
	# called 'Cerulean'
	Cerulean = turtle.Turtle()
	
	# set pencolor as Cerulean
	Cerulean.pencolor("Cerulean")
	
	# set pensize as 5
	Cerulean.pensize(5)
	
	# set turtleshape as turtle
	Cerulean.shape('turtle')
	pos = Cerulean.pos()

	# Turtle Purple initialization
	# instantiate a new turtle object
	# called 'Purple'
	Purple = turtle.Turtle()
	
	# set pencolor as Purple
	Purple.pencolor("Purple")
	
	# set pensize as 5
	Purple.pensize(5)
	
	# set turtleshape as turtle
	Purple.shape('turtle')
	
	# make the turtle invisible
	Purple.hideturtle()
	
	# don't draw when turtle moves
	Purple.penup()
	
	# move the turtle to a location 50
	# units away from Cerulean
	Purple.goto(pos[0]+50, pos[1])
	
	# make the turtle visible
	Purple.showturtle()
	
	# draw when the turtle moves
	Purple.pendown()

	# variable to store whether turtles
	# are in screen or not
	mT = True
	jT = True

	# loop for the game
	while mT and jT and sameposition(Cerulean, Purple):

		# coin flip for Cerulean
		coinCerulean = random.randrange(0, 2)

		# angle for Cerulean
		# random.randrange(0, 180)
		angleCerulean = 90

		# condition for left or right
		# based on coin
		if coinCerulean == 0:
			Cerulean.left(angleCerulean)
		else:
			Cerulean.right(angleCerulean)

		# coin flip for Purple
		coinPurple = random.randrange(0, 2)

		# angle for Purple
		# random.randrange(0, 180)
		anglePurple = 90

		# condition for left or right based
		# on coin
		if coinPurple == 0:
			Purple.left(anglePurple)
		else:
			Purple.right(anglePurple)

		# draw for Cerulean
		Cerulean.forward(50)

		# draw for Purple
		Purple.forward(50)

		# checking whether turtles are in the
		# screen or not
		mT = isInScreen(wn, Purple)
		jT = isInScreen(wn, Cerulean)

	# set pencolor for Purple and Cerulean as black
	Cerulean.pencolor("black")
	Purple.pencolor("black")

	# condition check for draw or win
	if jT == True and mT == False:
		# writing results
		Cerulean.write("Cerulean Won", True, align="center",
				font=("arial", 15, "bold"))
	
	elif mT == True and jT == False:
		
		# writing results
		Purple.write("Purple Won", True, align="center",
				font=("arial", 15, "bold"))
	else:
		# writing results
		Cerulean.write("Draw", True, align="center",
				font=("arial", 15, "bold"))
		Purple.write("Draw", True, align="center",
				font=("arial", 15, "bold"))

	# exit on close
	wn.exitonclick()


# Calling main function
main()
