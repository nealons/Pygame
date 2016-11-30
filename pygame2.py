import sys, pygame
import pygame
from pygame import *
from pygame.sprite import *
import random

class Breakout():
	def main(self):
		gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple
		score = 0
		max_lives = 3
		xspeed_init = 5
		yspeed_init = 5
		bat_speed = 20
		pygame.init()
		bat = pygame.image.load("paddle-hd.png").convert()
		ball = pygame.image.load("red_ball.png").convert()
		batrect = bat.get_rect()
		ballrect = ball.get_rect()
		size = width, height = 640, 480
		wall = Wall().build_wall()

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

			#CTha
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
				yspeed = yspeed_init
				ballrect.center = width * random.random(), height / 3
				if lives == 0:
					gameover = pygame.font.Font(None, 70).render("Game Over", True, (0, 255, 255))
					gameoverrect = gameover.get_rect()
					gameoverrect = gameoverrect.move(width / 2 - gameoverrect.center[0], height / 3)
					screen.blit(gameover, gameoverrect)
					pygame.display.flip()

					while 1:
						restart = False
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_ESCAPE:
									sys.exit()
								if not (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
									restart = True
						if restart:
							wall.build_wall(width)
							lives = max_lives
							score = 0
							break

			if xspeed > 0 and ballrect.left < 0:
				xspeed = -xspeed
				pong.play(0)

			if xspeed > 0 and ballrect.right > width:
				xspeed = -xspeed
				pong.play(0)

			#check if ball has hit wall, if it does delete brick and change direction

			index = ballrect.collidelist(wall.brickrect)
			if index != -1:
				if ballrect.center[0] > wall.brickrect[index].right or ballrect.center[0] < wall.brickrect[index].left:
					xspeed = -xspeed
				else:
					yspeed = -yspeed
				pong.play(0)
				wall.brickrect[index:index + 1] = []
				score += 10

			scoretext = pygame.font.Font(None, 40).render(str(score), True, (0, 255, 255))
			scoretextrect = scoretext.get_rect()
			scoretextrect = scoretext.rect.move(width - scoretextrect.right, 0)
			screen.blit(scoretext, scoretextrect)

			for i in range(0, len(wall.brickrect)):
				screen.blit(wall.brick, wall.brickrect[i])

			if wall.brickrect == []:
				wall.build_wall(width)
				xspeed = xspeed_init
				yspeed = yspeed_init
				ballrect.center = width / 2, height / 3

			screen.blit(ball, ballrect)
			screen.blit(bat, batrect)
			pygame.display.flip()

class Wall():

	def __init__(self):
		self.brick = pygame.image.load("brick.jpeg").convert()
		brickrect = self.brick.get_rect()
		self.bricklength = brickrect.right - brickrect.left
		self.brickheight = brickrect.bottom - brickrect.top

		
	def build_wall(brick, self, width):
		x_position = 0
		y_position = 60
		adj = 0
		self.brickrect = []
		for i in range (0, 52):
			if x_position > width:
				if adj == 0:
					adj = self.bricklength / 2
				else:
					adj = 0
				x_position  = -adj
				y_position += self.brickheight

			self.brickrect.append(self.brick.get_rect())
			self.brickrect[i] = self.brickrect[i].move(x_position, y_position)
			x_position = x_position + self.bricklength

if __name__ == '__main__':
	breakout = Breakout()
	breakout.main()







#Allows User to end game
gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True




#required
pygame.quit()
quit()				#exits python