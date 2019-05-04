import pygame
pygame.init()


Height = 600
Width = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


Spaceship_img = pygame.image.load("NewSpaceship.png")
EnemySpaceship_img = pygame.image.load("enemy_ship.png")
Friendly_Bullet_img = pygame.image.load("Spaceship_Bullet.png")


class Player(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.transform.scale(Spaceship_img, (150, 125))
			#self.image = Spaceship_img
			self.rect = self.image.get_rect()
			self.rect.center = (Width / 2, Height - 30)
			

		def update(self):
			self.speedx = 0
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.speedx = -4
			if keys[pygame.K_RIGHT]:
				self.speedx = 4
			self.rect.x += self.speedx
			if self.rect.right > Width + 50:
				self.rect.right = Width + 50
			if self.rect.left < -50:
				self.rect.left = -50

		def shoot(self):
			bullet = Bullet(self.rect.centerx, self.rect.top + 65)
			all_sprites.add(bullet)
			bullets.add(bullet)



class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(EnemySpaceship_img, (50, 30))
		self.rect = self.image.get_rect()
		self.rect.right = x
		self.rect.top = y
		#self.rect.center = (-self.rect.width / 2, Height / 3)

	def update(self):
		#enemy = Enemy(-self.rect.width / 2, Height / 3)
    	#set variable so that each time it runs, the spaceship's spawn point and endpoint is different
		self.speedx = 3
		self.rect.x += self.speedx
		if self.rect.right > Width:
			self.rect.right = Width





class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Friendly_Bullet_img, (20, 40))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        

    def update(self):
    	self.speedy = -10
    	self.rect.y += self.speedy
    	if self.rect.bottom < 0:
    		self.kill()

		

			


screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Galaga")
clock = pygame.time.Clock()



all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#enemy = Enemy(-self.rect.width / 2, Height / 3)
#another for loop/ divisible by 5 and store previous
# def this function
for i in range(0, 5):
	shipwidth = 50
	enemy = Enemy(-25 - shipwidth * i, Height / 3)
	all_sprites.add(enemy)
	enemies.add(enemy)
	#pygame.time.delay(100)



#Game Loop
run = True
while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()


	




	all_sprites.update()


	hits = pygame.sprite.groupcollide(enemies, bullets, True, True)

	#hits = pygame.sprite.collide(player, enemies, False)
	#if hits:
		#running = False


	screen.fill(BLACK)

	all_sprites.draw(screen)

	pygame.display.flip()


pygame.quit()

