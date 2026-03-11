import pygame
import config

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(config.GRAY)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args):
        pass

class LevelOne:
    def __init__(self):
        super().__init__()

        self.obstacles = pygame.sprite.Group()

        level_data = [
            (200, 200, 400, 400),
            (800, 400, 50, 200),
            (300, 500, 150, 150)
        ]

        for obs in level_data:
            wall = Obstacle(*obs)
            self.obstacles.add(wall)