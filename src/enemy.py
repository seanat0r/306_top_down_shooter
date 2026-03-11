import config
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        enemy_color = config.RED

        points = [(25, 0), (0, 50), (50, 50)]

        pygame.draw.polygon(self.image, enemy_color, points)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hp = config.ENEMY_HEALTH
        self.speed = config.ENEMY_SPEED
        self.speed_factor = config.ENEMY_SPEED_FACTOR
        self.pos = pygame.Vector2(x, y)

    def update(self, player_pos):
        direction = pygame.Vector2(player_pos) - self.pos

        if direction.length() > 0:
            veolocity = direction.normalize() * self.speed
            self.pos += veolocity 

            self.rect.center = self.pos
        

    def look_at(self, target_pos):
        directions = pygame.Vector2(target_pos) - self.rect.center
        angle = directions.angle_to(pygame.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.orginal_image, angle)

    def take_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()