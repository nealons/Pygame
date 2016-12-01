import math
import pygame 
import sys 
from pygame.sprite import *
from random import *
import os, sys

#colors
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
		super().__init__()
		self.image = pygame.Surface([brickw, brickh])
		self.image.fill(color) 
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Ball(pygame.sprite.Sprite):
	speed = 17.0
	x = 0.0
	y = 180.0
	direction = 250
	width = 10
	height = 10

	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(mustard)
		self.rect = self.image.get_rect()
		self.screenheight = pygame.display.get_surface().get_height()
		self.screenwidth = pygame.display.get_surface().get_width()

	def bounce(self, diff):
		self.direction = (180-self.direction) % 360
		self.direction -= diff

	def update(self):
		direction_radians = math.radians(self.direction)
		self.x += self.speed * math.sin(direction_radians)
		self.y -= self.speed * math.cos(direction_radians)

		self.rect.x = self.x
		self.rect.y = self.y

		if self.y <= 0:
			self.bounce(0)
			self.y = 1

		if self.x <= 0:
			self.direction = (360 - self.direction) % 360
			self.x = 1

		if self.x > self.screenwidth - self.width:
			self.direction = (360 - self.direction) % 360
			self.x = 1

		if self.x > self.screenwidth - self.width:
			self.direction = (360 - self.direction) % 360
			self.x = self.screenwidth - self.width - 1
			self.x = self.screenwidth -self.width - 1 

		if self.y > 600:
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
		position = pygame.mouse.get_pos()
		self.rect.x = position[0] #MAKE CENTER OF BAR

		if self.rect.x > self.screenwidth1 - self.width:
			self.rect.x = self.screenwidth1 - self.width

		if pygame.sprite.spritecollide(ball1, bricks, True):
			score += 1

pygame.init()


#mixer.music.load('Michigan.wav')
#mixer.music.play(-1)
#mixer.music.set_volume(5)

gameDisplay = pygame.display.set_mode([800, 600])

pygame.display.set_caption('Nealon\'s Brickbreaker Game!')

pygame.mouse.set_visible(0)

font = pygame.font.Font(None, 30)
score = 0
background = pygame.Surface(gameDisplay.get_size())
#sound = pygame.mixer.music.load('beep-08b.wav')
#sound.init()
#sound.pre_init(frequency=22050, size= -16, channels=2, buffer=4096)
#sound.set_volume(10)

#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
#bg_music = pygame.mixer.Sound("Michigan.wav")
#pygame.mixer.Sound.play(bg_music, loops = 0)
#pygame.mixer.Sound.play(bg_music, loops=-1)

bricks = pygame.sprite.Group()
ball = pygame.sprite.Group()
sprites = pygame.sprite.Group()

user1 = Paddle()
sprites.add(user1)

ball1 = Ball()
sprites.add(ball1)
ball.add(ball1)

top_brick = 80
brickcount = 16

for row in range(3):
	for columns in range(0, brickcount):
		brick = Brick(forest, columns * (brickw + 2) + 1, top_brick)
		bricks.add(brick)
		sprites.add(brick)

	top_brick +=brickh + 2

clock = pygame.time.Clock()
game_over = False
exit_program = False

while not exit_program:
	clock.tick(30)

	for events in pygame.event.get():
		if events.type ==pygame.QUIT:
			exit_program = True

	if not game_over:
		user1.update()
		game_over = ball1.update()

	if game_over:
		game_over_text = font.render('Game Over! Thanks for playing! :)', True, thistle)
		go_text_position = game_over_text.get_rect(centerx = 420)
		go_text_position.top = 300
		gameDisplay.blit(game_over_text, go_text_position)

	if pygame.sprite.spritecollide(user1, ball, False):
		diff = (user1.rect.x + user1.width/2) - (ball1.rect.x + ball1.width/2)

		ball1.rect.y = gameDisplay.get_height() - user1.rect.height - ball1.rect.height - 1
		ball1.bounce(diff)

	hitbricks = pygame.sprite.spritecollide(ball1, bricks, True)

	if pygame.sprite.spritecollide(ball1, bricks, True):
		score += 1

	#if hitbricks == True:
	#	sound.mixer.music.play(0)

	if len(hitbricks) > 0:
		ball1.bounce(0)

	if len(bricks) == 0:
		game_over = True
		game_win_text = font.render('You win! Congratulations! Thanks for playing! :)', True, thistle)
		gw_text_position = game_win_text.get_rect(centerx = 400)
		gw_text_position.top = 300
		gameDisplay.blit(game_win_text, gw_text_position)

	gameDisplay.fill(leather)
	t = font.render('Score:' + str(score), False, black)
	gameDisplay.blit(t, (320, 0))


	sprites.draw(gameDisplay)
	pygame.display.flip()
 
pygame.quit()




