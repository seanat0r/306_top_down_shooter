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

class LevelExit(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 255, 0, 150))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args):
        pass

class LevelOne:
    def __init__(self):
        super().__init__()

        self.obstacles = pygame.sprite.Group()

        level_data = [
            (200, 100, 150, 150),
            (400, 400, 40, 200),
            (200, 100, 100, 100),
            (900, 450, 200, 150),
        ]

        for obs in level_data:
            wall = Obstacle(*obs)
            self.obstacles.add(wall)

        self.exit_portal = LevelExit(config.WIDTH - 40, config.HEIGHT // 2 - 50, 40, 100)

class LevelTwo:
    def __init__(self):
        super().__init__()

        self.obstacles = pygame.sprite.Group()
        level_data = [
            (800, 100, 40, 400), 
            (600, 500, 350, 40),
            (950, 150, 150, 150), 
            (500, 50, 40, 150),

            (150, 200, 300, 40), 
            (150, 200, 40, 300), 
            (150, 460, 300, 40), 
        ]

        for obs in level_data:
            self.obstacles.add(Obstacle(*obs))