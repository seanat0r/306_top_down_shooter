import config
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
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
        self.ammo = config.PLAYER_START_AMMO
        self.max_ammo = config.PLAYER_MAX_AMMO
        self.is_reloading = False
        self.reload_start_time = 0
        self.reload_duration = config.RELOAD_DURATION
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

    def update(self, *args):

        if self.is_reloading:
            now = pygame.time.get_ticks()
            if now - self.reload_start_time >= self.reload_duration:
                self.ammo = self.max_ammo
                self.is_reloading = False
                print("Nachladen beendet!")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed

    def shoot(self):
        if self.ammo > 0 and not self.is_reloading:
            self.ammo -= 1
            return True
        return False
    
    def reload(self):
        if not self.is_reloading:
            self.is_reloading = True
            self.reload_start_time = pygame.time.get_ticks()
            print("Lade nach!")