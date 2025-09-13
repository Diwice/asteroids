import pygame
from sys import exit
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

	pygame.init()

	dt = 0
	timeObj = pygame.time.Clock()

	asteroids,updatable,drawable,shots = pygame.sprite.Group(),pygame.sprite.Group(),pygame.sprite.Group(),pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	Shot.containers = (shots,updatable,drawable)
	Asteroid.containers = (asteroids,updatable,drawable)
	AsteroidField.containers = (updatable)

	playerObj = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	asteroidFieldObj = AsteroidField()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:

		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				return

		screen.fill(color=(0,0,0))

		for obj in drawable :
			obj.draw(screen)

		for obj in updatable :
			obj.update(dt)

		for obj in asteroids :
			obj.collides(playerObj) and exit("Game over!")
			for bullet in shot :
				if obj.collides(bullet) :
					obj.split(dt)
					bullet.kill()

		pygame.display.flip()
		dt = timeObj.tick(60)/1000

if __name__ == "__main__":
	main()
