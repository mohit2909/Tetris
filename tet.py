import pygame,sys
from random import randrange as rand
cell_size =	18
cols =		10
rows =		22
maxfps = 	1130

colors = [
(0,   0,   0  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) # Helper color for background grid
]

# Define the shapes of the single parts
tetris_shapes = [
	[[1, 1, 1],
	 [0, 1, 0]],
	
	[[0, 2, 2],
	 [2, 2, 0]],
	
	[[3, 3, 0],
	 [0, 3, 3]],
	
	[[4, 0, 0],
	 [4, 4, 4]],
	
	[[0, 0, 5],
	 [5, 5, 5]],
	
	[[6, 6, 6, 6]],
	
	[[7, 7],
	 [7, 7]]
]
block=[]
stone_x=0
stone_y=0
stone=[None]*100
screen=pygame.display.set_mode((800,600))
def select_piece():
	block_number=rand(0,6)
	block=tetris_shapes[block_number]
	c=len(block[0])
	stone_x=int(cols/2)-int(len(tetris_shapes[block_number][0]))
	stone_y=0
	draw_matrix(tetris_shapes[block_number],(cols/2-len(tetris_shapes[block_number][0]),0))
def draw_matrix(matrix, offset):
		off_x, off_y  = offset
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(
						screen,
						colors[val],
						pygame.Rect(
							(off_x+x) *
							  cell_size,
							(off_y+y) *
							  cell_size, 
							cell_size,
							cell_size),0)
def move_left():
	global stone_x
	global block
	newx=stone_x-1
	if newx<0:
		newx=0
	if newx > cols-block[0] :
				newx = cols - len(block[0])
	stone_x=newx			
	draw_matrix(block[0],(stone_x,0))


def move_right():
	newx=stone_x+1
	if newx<0:
		newx=0
	if newx > cols - len(stone[0]):
				new_x = cols - len(stone[0])

def rotate_clockwise(shape):
	return [ [ shape[y][x]
			for y in xrange(len(shape)) ]
		for x in xrange(len(shape[0]) - 1, -1, -1) ]
select_piece()
move_left()
run=True
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False
	pygame.display.update()

