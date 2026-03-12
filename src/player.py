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

        self.pos = pygame.Vector2(config.WIDTH // 2, config.HEIGHT // 2)
        self.rect.center = self.pos

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

    def update(self, target_pos, dt, obstacles, *args):

        if self.ammo <= 0 and not self.is_reloading:
            self.reload()

        if self.is_reloading:
            now = pygame.time.get_ticks()
            if now - self.reload_start_time >= self.reload_duration:
                self.ammo = self.max_ammo
                self.is_reloading = False
                print("Nachladen beendet!")

        direction = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: direction.y -= 1
        if keys[pygame.K_s]: direction.y += 1
        if keys[pygame.K_a]: direction.x -= 1
        if keys[pygame.K_d]: direction.x += 1

        if direction.length() > 0:
            direction = direction.normalize()

            # --- 1. X-ACHSE BEWEGEN ---
            self.pos.x += direction.x * self.speed * dt
            self.rect.centerx = self.pos.x
            
            # FRISCHE Abfrage für X
            hit_list_x = pygame.sprite.spritecollide(self, obstacles, False)
            for wall in hit_list_x:
                if direction.x > 0: # Nach rechts
                    self.rect.right = wall.rect.left
                if direction.x < 0: # Nach links
                    self.rect.left = wall.rect.right
                self.pos.x = self.rect.centerx 

            # --- 2. Y-ACHSE BEWEGEN ---
            self.pos.y += direction.y * self.speed * dt
            self.rect.centery = self.pos.y

            # FRISCHE Abfrage für Y (ganz wichtig!)
            hit_list_y = pygame.sprite.spritecollide(self, obstacles, False)
            for wall in hit_list_y:
                if direction.y > 0: # Nach unten
                    self.rect.bottom = wall.rect.top
                if direction.y < 0: # Nach oben
                    self.rect.top = wall.rect.bottom
                self.pos.y = self.rect.centery

        screen_rect = pygame.Rect(0,0, config.WIDTH, config.HEIGHT)
        self.rect.clamp_ip(screen_rect)

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