import sys, pygame
import pygame
from pygame import *
from pygame.sprite import *
import random
pygame.init()

class Breakout():
	def main(self):
		gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple
		score = 0
		max_lives = 3
		xspeed_init = 5
		yspeed_init = 5
		bat_speed = 20
		
		bat = pygame.image.load("downloads/paddle-hd.png").convert()
		ball = pygame.image.load("downloads/red_ball.png").convert()
		batrect = bat.get_rect()
		ballrect = ball.get_rect()

		wall = Wall()

		wall.buld_wall(800)

		#game loop
		batrect = batrect.move((width / 2) - (batrect.right / 2), (height - 20))
		ballrect = ballrect.move((width / 2, (height / 2)))
		xspeed = xspeed_init
		yspeed = yspeed_init
		lives = max_lives
		clock = pygame.time.Clock()
		pygame.key.set_repeat(1,30)
		pygame.mouse_set_visible(0)

		while 1:
			clock.tick(60)

			#process key presses
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type ==pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
				if event.key == pygame.K_LEFT:
					batrect = batrect.move(-bat_speed, 0)
					if (batrect.left < 0):
						batrect.left = 0
				if event.key == pygame.K_RIGHT:
					batrect = batrect.move(bat_speed, 0)
					if (batrect.right > width):
						batrect.right = width

			#is bat hitting the ball?
			if ballrect.bottom >= batrect.top and ballrect.bottom <= batrect.bottom and ballrect.right >= batrect.left and ballrect.left <= batrect.right:
				yspeed = -yspeed
				pong.play(0)
				ballpos = ballrect.center[0] - batrect.center[0]
				if ballpos > 0:
					if ballpos > 30:
						xspeed = 6
					elif ballpos > 23:
						xspeed = 6
					elif ballpos > 17:
						xspeed = 5

				else:
					if ballpos < -30:
						xspeed = -6
					elif ballpos < -23:
						xspeed = -6
					elif ballpos < -17:
						xspeed = -6

			#C
			ballrect = ballrect.move(xspeed, yspeed)
			if ballrect.left < 0 or ballrect.right > width:
				xspeed = -xspeed
				pong.play(0)
			if ballrect.top < 0:
				yspeed = -yspeed
				pong.play(0)

			#if you LOOZE
			if ballrect.top > height:
				lives -= 1

				#new ball now
				xspeed = xspeed.init
				fate = random.random()
				if fate > 0.5:
					xspeed = -xspeed
				elif:
					xspeed = xspeed
				yspeed = yspeed_init










#Allows User to end game
gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True




#required
pygame.quit()
quit()				#exits python