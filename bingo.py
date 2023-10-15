import turtle, time, sys, os
from tkinter import PhotoImage
from turtle import Shape
from numbers import *
from imgdraw import *
# from convert import *

t = time.time()

print("bingo starting")

scr = turtle.Screen()
scr.setup(1000,800)
scr.colormode(255)
scr.title("Spanish Bingo")
scr.tracer(0)

BINGO_TITLE = "BINGO"

UPPER_LEFT = (X_SIZE*-2, Y_SIZE*1)

bingo = turtle.Turtle()

file_name = 0

# draws image based on row and column
def draw_image(r, c, ns, lang):
	index = c * 5 + r

	pic = f"images/{ns[index]}{lang}.gif"

	scr.register_shape(pic)
	bingo.shape(pic)
	bingo.stamp()

def draw_grid():

	#draws a grid around each image afterwards
	bingo.penup()
	
	GRID_UPPER_LEFT = (X_SIZE*-2.5, Y_SIZE*1.5)
	bingo.goto(GRID_UPPER_LEFT)

	bingo.width(4)

	for i in range(6):
		bingo.pendown()
		bingo.forward(X_SIZE*5)
		bingo.penup()
		bingo.goto(GRID_UPPER_LEFT)
		bx, by = bingo.pos()

		bingo.goto(bx, by-(Y_SIZE*(i+1)))

	bingo.right(90)
	bingo.goto(GRID_UPPER_LEFT)
	
	for i in range(6):
		bingo.pendown()
		bingo.forward(Y_SIZE*5)
		bingo.penup()
		bingo.goto(GRID_UPPER_LEFT)

		bx, by = bingo.pos()
		bingo.goto(bx+(X_SIZE*(i+1)), by)

def draw_title():
	
	# set location
	bingo.penup()
	bingo.goto((0,Y_SIZE*3))
	bingo.pendown()

	pic = f"images/title.gif"
	scr.register_shape(pic)
	bingo.shape(pic)
	bingo.stamp()

	bingo.penup() 

def save_board():
	# take entire board as picture
	# save to file
	global file_name
	img = bingo.getscreen()

	img.getcanvas().postscript(file=f"done/{file_name}.eps")
	# img.getcanvas().postscript(file=f"{file_name}.eps")

	file_name +=1

def do_bingo(lang):
	# get the list of numbers used for images
	# ex: 4, 16, 23, 7, 6...
	nums = get_shuffled_numbers()

	for row in range(5):
		bingo.penup()
		bingo.goto(UPPER_LEFT)
		bx, by = bingo.pos()
		bingo.goto(bx, by - (Y_SIZE * (row)))

		for column in range(5):
			bingo.pendown()
			
			draw_image(row, column, nums, lang)

			bingo.penup()
			bx, by = bingo.pos()
			if column == 4 and row == 4:
				break

			bingo.goto(bx + X_SIZE, by)

	draw_grid()
	draw_title()

	scr.update()
	save_board()
	bingo.reset()

bingo.reset()

boards = 2
for i in range(boards):
	do_bingo('sf')
	do_bingo('ef')

for i in range(boards):
	do_bingo('sb')
	do_bingo('eb')

print(time.time()-t)
turtle.done()
print("Done")