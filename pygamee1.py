import math
import pygame 
import sys 
from pygame.sprite import *
from random import *
import os, sys

#colors I hope you enjoy them I put a lot of thought into them
leather = (205, 133, 63)
mustard = (255, 215, 0)
forest = (34, 139, 34)
thistle = (216, 191, 216)
black = (0, 0, 0)

#Size of the bricks
brickw = 48
brickh = 20

class Brick(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super().__init__() #you have to do this 
		self.image = pygame.Surface([brickw, brickh]) #creates the brick image
		self.image.fill(color) 
		self.rect = self.image.get_rect() #gets a rectangle object with the image specifications
		self.rect.x = x
		self.rect.y = y

class Ball(pygame.sprite.Sprite):
	speed = 11.0 #speed of ball
	x = 180.0 #initial location of ball
	y = 180.0
	direction = 210 #initial direction of ball
	width = 10
	height = 10

	def __init__(self): #
		super().__init__()
		self.image = pygame.Surface([self.width, self.height]) #creates image
		self.image.fill(mustard)
		self.rect = self.image.get_rect() 
		self.screenheight = pygame.display.get_surface().get_height() 
		self.screenwidth = pygame.display.get_surface().get_width()

	def bounce(self, bounce_where):
		self.direction = (180-self.direction) % 360 #ball bounces off surfaces
		self.direction -= bounce_where

	def update(self):
		direction_radians = math.radians(self.direction)
		self.x += self.speed * math.sin(direction_radians) #changes x and y as function of speed and direction
		self.y -= self.speed * math.cos(direction_radians)

		self.rect.x = self.x #makes the ball what x and y are
		self.rect.y = self.y

		if self.y <= 0: #bounces off top of screen
			self.bounce(0)
			self.y = 1

		if self.x <= 0: #bounces off left screen
			self.direction = (360 - self.direction) % 360
			self.x = self.x + 20

		if self.x > self.screenwidth - self.width: #bounces off right screen
			self.direction = (360 - self.direction) % 360
			self.x = self.x - 20

		if self.x > self.screenwidth - self.width:
			self.direction = (360 - self.direction) % 360
			self.x = self.screenwidth - self.width - 1
			self.x = self.screenwidth -self.width - 1 

		if self.y > 600: #fell off screen
			return True
		else:
			return False

class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.width = 75
		self.height = 15
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(mustard)

		self.rect = self.image.get_rect() 
		self.screenheight1 = pygame.display.get_surface().get_height()
		self.screenwidth1 = pygame.display.get_surface().get_width()

		self.rect.x = 0
		self.rect.y = self.screenheight1 - self.height

	def update(self):
		position = pygame.mouse.get_pos() #get mouse location
		self.rect.x = position[0] #MAKE CENTER OF BAR

		if self.rect.x > self.screenwidth1 - self.width: 
			self.rect.x = self.screenwidth1 - self.width



pygame.init() #initializes pygame library



gameDisplay = pygame.display.set_mode([800, 600]) #creates game screen

pygame.display.set_caption('Nealon\'s Brickbreaker Game!') #title

pygame.mouse.set_visible(0) #mouse disappears

font = pygame.font.Font(None, 30) #font information
score = 0 #score variable initializes
background = pygame.Surface(gameDisplay.get_size()) #creates background


#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
#bg_music = pygame.mixer.Sound("Michigan.wav")
#pygame.mixer.Sound.play(bg_music, loops = 0)

bricks = pygame.sprite.Group() #sprite lists
ball = pygame.sprite.Group()
sprites = pygame.sprite.Group()

user1 = Paddle()  #creates paddle object
sprites.add(user1)

ball1 = Ball() #creates ball object
sprites.add(ball1)
ball.add(ball1)

top_brick = 80
brickcount = 16

for row in range(3): #creates wall of bricks
	for columns in range(0, brickcount):
		brick = Brick(forest, columns * (brickw + 2) + 1, top_brick)
		bricks.add(brick)
		sprites.add(brick)

	top_brick +=brickh + 2

clock = pygame.time.Clock()
game_over = False
exit_program = False

while not exit_program: #game loop
	clock.tick(30)

	for events in pygame.event.get(): 
		if events.type ==pygame.QUIT:
			exit_program = True

	if not game_over: #updates paddle and ball 
		user1.update()
		game_over = ball1.update()

	if game_over: #prints game over but for some reason it doesn't work 
		game_over_text = font.render('Game Over! Thanks for playing! :)', True, thistle)
		go_text_position = game_over_text.get_rect(centerx = 420)
		go_text_position.top = 300
		gameDisplay.blit(game_over_text, go_text_position)

	if pygame.sprite.spritecollide(user1, ball, False): #see if ball and paddle collide
		bounce_where = (user1.rect.x + user1.width/2) - (ball1.rect.x + ball1.width/2)

		ball1.rect.y = gameDisplay.get_height() - user1.rect.height - ball1.rect.height - 1
		ball1.bounce(bounce_where)
		#all the above checks to see where teh ball hits the paddle

	hitbricks = pygame.sprite.spritecollide(ball1, bricks, True) #keeps track of ball and brick hits

	for x in hitbricks: #increments through hits for score
		score +=1


	if len(hitbricks) > 0: #bounces the ball if brick hits 
		ball1.bounce(0)

	if len(bricks) == 0: #game over when bricks are all gone and congratulations text is printed
		game_over = True
		game_win_text = font.render('You win! Congratulations! Thanks for playing! :)', True, thistle)
		gw_text_position = game_win_text.get_rect(centerx = 400)
		gw_text_position.top = 300
		gameDisplay.blit(game_win_text, gw_text_position)

	gameDisplay.fill(leather) #screen background
	t = font.render('Score:' + str(score), False, black) #score is printed
	gameDisplay.blit(t, (320, 0)) #score is printed on screen


	sprites.draw(gameDisplay) #draws the whole time
	pygame.display.flip() #flips screen because we have to
 
pygame.quit()




