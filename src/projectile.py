import pygame
import config

class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, config.COLOR2, (5,5), 5)
        self.rect = self.image.get_rect(center=start_pos)
        
        self.pos = pygame.Vector2(start_pos)
        direction = pygame.Vector2(target_pos) - self.pos

        if direction.length() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(1, 0)

        self.speed = config.BULLET_SPEED

    def update(self, *args):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill