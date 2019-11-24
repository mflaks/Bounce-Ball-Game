from tkinter import *
import random
import time

root = Tk()
root.title('Bounce')

root.resizable(0,0)						# lock the window size (x and y)
root.wm_attributes('-topmost',1)		# keep the window always in front all other applications

canvas = Canvas(root, width = 500, height = 500, bd = 0 , highlightthickness = 0, bg= 'white')
canvas.pack()
root.update()

screen_width = canvas.winfo_width()
screen_height = canvas.winfo_height()

game_over = False


class Ball:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_oval(0,0,10,10, fill= color)		# create ball
		start_y = [150,200,250,300,350]
		random.shuffle(start_y)
		self.canvas.move(self.id,start_y[0],start_y[1])							# move ball to the start point
		y = -3
		start_x = [-3,-2,-1,0,1,2,3]										# random choose the angle to move the ball (x).  Y is fixed
		random.shuffle(start_x)		
		self.x = start_x[0]
		self.y = y
	
			
	def play(self):
		self.pos_ball = self.canvas.coords(self.id)
		print(self.pos_ball)
		if self.pos_ball[1] <= 0:
			self.y = -self.y
		if self.pos_ball[3] >= screen_height:
			global game_over
			game_over = True
		if self.pos_ball[0] <=0:
			self.x = -self.x
		if self.pos_ball[2] >= screen_width:
			self.x = -self.x
		self.canvas.move(self.id, self.x, self.y)
		
		
	def ball_hit_paddle(self):
		if self.pos_ball[2]>=pos_paddle[0] and self.pos_ball[0]<=pos_paddle[2]:
			print('tru')
			if self.pos_ball[3]>=pos_paddle[1] and self.pos_ball[1]<=pos_paddle[3]:
				self.y = -3

		
class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0,0,100,12, fill = color)
		self.canvas.move(self.id,200,400)
		self.x = 0
		self.y = 0
		def right(event):
			global x1 
			x1 = 3
		self.canvas.bind_all('<Right>', right)	
			
	def move_paddle(self):
		global pos_paddle
		pos_paddle = self.canvas.coords(self.id)
		def right(event):
			if pos_paddle[2] >= screen_width:
				self.x = 0
			else:
				self.x = 10
		def left(event):
			if pos_paddle[0] <= 0: 
				self.x = 0
			else:
				self.x = -10
		self.canvas.bind_all('<Right>', right)
		self.canvas.bind_all('<Left>', left)
		self.canvas.move(self.id, self.x, self.y)
		self.x = 0

b1 = Ball(canvas, 'red')
b2 = Ball(canvas, 'green')
# b3 = Ball(canvas, 'pink')

p1 = Paddle(canvas, 'blue')

while True:
	if game_over == True: 
		break
	else:
		b1.play()
		b2.play()
		# b3.play()
		p1.move_paddle()
		b1.ball_hit_paddle()
		b2.ball_hit_paddle()
		# b3.ball_hit_paddle()
		root.update()
		time.sleep(0.03)
	
	

	
	
root.mainloop()
