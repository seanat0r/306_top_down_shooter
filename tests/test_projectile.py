import pytest
import pygame
from src.projectile import Projectile
from src import config

@pytest.fixture(autouse=True)
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600), pygame.NOFRAME) # Screen-Größe für Boundary-Check
    yield
    pygame.quit()

def test_projectile_initialization():
    start = (100, 100)
    target = (200, 100)
    bullet = Projectile(start, target)
    
    assert bullet.direction.x == 1.0
    assert bullet.direction.y == 0.0

def test_projectile_movement():
    start = pygame.Vector2(100, 100)
    target = (200, 100)
    bullet = Projectile(start, target)
    
    dt = 1.0

    bullet.update(None, dt)
    
    expected_x = start.x + config.BULLET_SPEED
    
    assert bullet.pos.x == expected_x
    assert bullet.rect.centerx == round(expected_x)

def test_projectile_zero_direction():
    bullet = Projectile((100, 100), (100, 100))
    assert bullet.direction.length() == 1.0