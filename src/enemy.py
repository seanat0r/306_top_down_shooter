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

        self.hitbox = pygame.Rect(0, 0, 30, 30)
        self.hitbox.center = (x, y)

        self.hp = config.ENEMY_HEALTH
        self.speed = config.ENEMY_SPEED
        self.speed_factor = config.ENEMY_SPEED_FACTOR
        self.pos = pygame.Vector2(x, y)

    def update(self, player_pos, dt, obstacles, *args):
        direction = pygame.Vector2(player_pos) - self.pos

        if direction.length() > 0:
            velocity = direction.normalize() * self.speed * dt

            # --- X-ACHSE BEWEGEN ---
            self.pos.x += velocity.x
            self.hitbox.centerx = round(self.pos.x)
        
            hit_x = False
            for wall in obstacles:
                if self.hitbox.colliderect(wall.rect):
                    hit_x = True
                    if velocity.x > 0: # Nach rechts gelaufen
                        self.hitbox.right = wall.rect.left
                    if velocity.x < 0: # Nach links gelaufen
                        self.hitbox.left = wall.rect.right
                    self.pos.x = float(self.hitbox.centerx)

            # SCHLAUE LOGIK: Wenn X blockiert ist, hilf bei der Y-Bewegung
            if hit_x:
                # Wir schauen, in welche Richtung der Gegner sowieso auf der Y-Achse wollte
                y_slide = 1 if velocity.y >= 0 else -1
                # Wir geben einen Bonus-Schub auf Y, damit er um die Ecke gleitet
                self.pos.y += y_slide * self.speed * dt * 0.5

            # --- Y-ACHSE BEWEGEN ---
            self.pos.y += velocity.y
            self.hitbox.centery = round(self.pos.y)
        
            hit_y = False
            for wall in obstacles:
                if self.hitbox.colliderect(wall.rect):
                    hit_y = True
                    if velocity.y > 0: # Nach unten gelaufen
                        self.hitbox.bottom = wall.rect.top
                    if velocity.y < 0: # Nach oben gelaufen
                        self.hitbox.top = wall.rect.bottom
                    self.pos.y = float(self.hitbox.centery)

            # SCHLAUE LOGIK: Wenn Y blockiert ist, hilf bei der X-Bewegung
            if hit_y:
                x_slide = 1 if velocity.x >= 0 else -1
                self.pos.x += x_slide * self.speed * dt * 0.5

            # --- GRAFIK & ROTATION ---
            angle = direction.angle_to(pygame.Vector2(0, -1))
            self.image = pygame.transform.rotate(self.original_image, angle)
        
            # Das grafische Rect wird NUR für das Zeichnen benutzt
            self.rect = self.image.get_rect(center=self.hitbox.center)

    def look_at(self, target_pos):
        directions = pygame.Vector2(target_pos) - self.rect.center
        angle = directions.angle_to(pygame.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.orginal_image, angle)

    def take_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
        return config.ENEMY_SCORE_VALUE