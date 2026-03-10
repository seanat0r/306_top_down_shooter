import config
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, weapon = False):
        super().__init__()
        # small sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH // 2, config.HEIGHT // 2)


        self.hp = config.PLAYER_HEALTH
        self.max_hp = config.PLAYER_HEALTH
        self.speed = config.PLAYER_SPEED
        self.is_alive = True
        self.weapon = weapon

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed