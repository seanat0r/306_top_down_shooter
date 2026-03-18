import pytest
import pygame
from src.player import Player

# Mini Setup
@pytest.fixture(autouse=True)
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    yield
    pygame.quit()

@pytest.fixture
def player():
    return Player()

# --- TEST FOR TAKING DMG ---

def test_take_damage(player):
    initial_hp = player.hp
    player.take_damage(1)
    assert player.hp == initial_hp - 1
    assert player.is_alive is True

def test_player_death(player):
    player.take_damage(player.hp)
    assert player.hp == 0
    assert player.is_alive is False

def test_hp_not_negative(player):
    player.take_damage(999)
    assert player.hp == 0

# --- TEST FOR SHOOTING ---

def test_shoot_reduces_ammo(player):
    initial_ammo = player.ammo
    success = player.shoot()
    assert success is True
    assert player.ammo == initial_ammo - 1

def test_shoot_fails_when_empty(player):
    player.ammo = 0
    success = player.shoot()
    assert success is False
    assert player.ammo == 0

def test_cannot_shoot_while_reloading(player):
    player.reload()
    success = player.shoot()
    assert player.is_reloading is True
    assert success is False