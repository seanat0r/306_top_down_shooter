import pytest
import pygame
from src.enemy import Enemy
from src import config

@pytest.fixture(autouse=True)
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    yield
    pygame.quit()

@pytest.fixture
def enemy():
    return Enemy(100, 100, 2)

# --- TEST DMG-LOGIC ---

def test_enemy_take_hit(enemy):
    initial_hp = enemy.hp
    score = enemy.take_hit(1)
    assert enemy.hp == initial_hp - 1
    assert score == config.ENEMY_SCORE_VALUE

def test_enemy_death(enemy):
    group = pygame.sprite.Group()
    group.add(enemy)
    
    enemy.take_hit(enemy.hp)
    assert enemy.hp <= 0
    assert enemy not in group

# --- TEST KI/ MOVMENT ---

def test_enemy_movement_towards_player(enemy):
    initial_pos = pygame.Vector2(enemy.pos)
    # Spieler ist rechts vom Gegner (200, 100)
    player_pos = (200, 100)
    dt = 1.0
    obstacles = [] 
    
    enemy.update(player_pos, dt, obstacles)
    
    assert enemy.pos.x > initial_pos.x
    assert enemy.pos.y == initial_pos.y

def test_enemy_hitbox_follows_pos(enemy):
    player_pos = (200, 200)
    enemy.update(player_pos, 1.0, [])
    
    assert enemy.hitbox.centerx == round(enemy.pos.x)
    assert enemy.hitbox.centery == round(enemy.pos.y)