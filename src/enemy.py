import config
import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        enemy_color = config.RED
        points = [(25, 0), (0, 50), (50, 50)]
        pygame.draw.polygon(self.original_image, enemy_color, points)

        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hp = config.ENEMY_HEALTH
        self.speed = config.ENEMY_SPEED
        self.speed_factor = config.ENEMY_SPEED_FACTOR
        self.pos = pygame.Vector2(x, y)

    def update(self, player_pos, *args):
        direction = pygame.Vector2(player_pos) - self.pos

        if direction.length() > 0:
            velocity = direction.normalize() * self.speed
            self.pos += velocity 

            angle = direction.angle_to(pygame.Vector2(0, -1))
            self.image = pygame.transform.rotate(self.original_image, angle)

            self.rect = self.image.get_rect(center=self.pos)
        

    def look_at(self, target_pos):
        directions = pygame.Vector2(target_pos) - self.rect.center
        angle = directions.angle_to(pygame.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.orginal_image, angle)

    def take_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
        return config.ENEMY_SCORE_VALUE
    
    def upgrade_speed(self, score):
        tenfold = score % 10
        if tenfold == 0:
            config.ENEMY_SPEED += self.speed_factor