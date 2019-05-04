

#ReadMe: Basically, we watched YouTube tutorials and read how to use pygames. The learning process was a bit overwhelming, so there isn't too much, however, we figured out the template for how we are going to run the game. 



#just_the_start
import pygame

pygame.init()
display_width = 500
display_height = 500
screen = pygame.display.set_mode((display_width, display_height))
black = (0, 0, 0)
white = (255, 255, 255)
done = False
height = 50
width = 50
x = 0
y = 500 - height
z = display_width - 550
r = display_height - 90
vel = 3
Spaceship_Width = 148
Spaceship_Height = 125



spaceshipImg = pygame.image.load("NewSpaceship.png")

def spaceship (z, r):
	screen.blit(spaceshipImg, (z, r))

pygame.display.update()

clock = pygame.time.Clock()


class projectile(object):
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.vel = 8 

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
	for bullet in bullets:
		bullet.draw(screen)

	pygame.display.update()

#MainLoop
bullets = []
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	for bullet in bullets:
		if bullet.y < 500 and bullet.y > 0:
			bullet.y += bullet.vel
		else: 
			bullets.pop(bullets.index(bullet))

	press = pygame.key.get_pressed()
	if press[pygame.K_LEFT] and z > -50: z -= 5
	if press[pygame.K_RIGHT] and z < display_width - 98: z += 5

	if press[pygame.K_SPACE]:
		if len(bullets) < 5:
			bullets.append(projectile(round(z + Spaceship_Width //2), round(r + Spaceship_Height //2), 6, (255, 255, 255)))
	

	#screen.fill(black)

	spaceship(z, r)

	pygame.display.update()

	clock.tick(60)

"""
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and y > 0: y -= vel
	if pressed[pygame.K_DOWN] and y < display_height: y += vel
	if pressed[pygame.K_RIGHT] and x < display_width: x += vel
	if pressed[pygame.K_LEFT] and x > 0: x -= vel

	#screen.fill(black)

	pygame.draw.rect(screen, (0, 128, 255), (x, y, width, height))
"""


	#pygame.display.update()
	
	#clock.tick(60)