import pygame
import random
import config
from src import Player, Projectile, Enemy, LevelOne, LevelTwo, UIManager

class Game:
    def __init__(self):
        pygame.init()
        self.ui_manager = UIManager()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Top-Down Shooter")
        self.clock = pygame.time.Clock()
        self.running = True

        self.notification_text = ""
        self.notification_timer = 0
        
        self.font = pygame.font.SysFont("Arial", 48, bold=True)    
        self.small_font = pygame.font.SysFont("Arial", 22, bold=True)

        self.state = "MENU"

    def new(self):
        """Initialisiert eine komplett neue Spielrunde"""
        self.current_enemy_speed = config.ENEMY_SPEED
        self.current_spawn_cooldown = config.SPAWN_COOLDOWN
        self.notification_text = ""
        self.notification_timer = 0

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.current_level_num = 1
        self.load_level(LevelOne())
        
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.last_spawn_time = 0

    def load_level(self, level_obj):
        self.current_level_obj = level_obj
        self.obstacles = self.current_level_obj.obstacles
        self.level_exit = getattr(level_obj, 'exit_portal', None)
        
        self.all_sprites.add(self.obstacles)
        if self.level_exit:
            self.all_sprites.add(self.level_exit)

    def run(self):
        while self.running:
            self.dt = self.clock.tick(60) / 1000.0
            self.events()

            match self.state:
                case "PAUSED":
                    self.draw_pause_screen()
                case "MENU":
                    self.draw_menu()
                case "PLAYING":
                    self.update()
                    self.draw()
                case "GAMEOVER":
                    self.draw_game_over()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    if self.state == "PLAYING":
                        self.state = "PAUSED"
                    elif self.state == "PAUSED":
                        self.state = "PLAYING"
                    else:
                        self.running = False 

            match self.state:
                case "PAUSED":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.state = "PLAYING"

                case "MENU":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.new()
                        self.state = "PLAYING"
            
                case "PLAYING":
                    # Shoot & Reload
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r and not self.player.is_reloading:
                            self.player.reload()
                
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.player.shoot():
                            mouse_pos = pygame.mouse.get_pos()
                            new_bullet = Projectile(self.player.rect.center, mouse_pos)
                            self.all_sprites.add(new_bullet)
                            self.bullets.add(new_bullet)

                case "GAMEOVER":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.state = "MENU"

    def update(self):
        current_time = pygame.time.get_ticks()
        
        # 1. Spawning
        if current_time - self.last_spawn_time > self.current_spawn_cooldown:
            self.spawn_enemy()
            self.last_spawn_time = current_time

        # 2. Movement & Logic
        self.all_sprites.update(self.player.rect.center, self.dt, self.obstacles)
        self.check_collisions()

        # 3. Level Exit Check
        if self.level_exit and pygame.sprite.collide_rect(self.player, self.level_exit):
            self.switch_to_level_two()

    def check_collisions(self):
        # Enemy vs Bulets
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for enemy in hits:
            self.score += enemy.take_hit(1)

            if self.score % 100 == 0 and self.score > 0:
                self.player.max_ammo += config.PLAYER_AMMO_FACTOR
                self.trigger_notification(f"UPGRADE: +{config.PLAYER_AMMO_FACTOR} MAX-AMMO!\n WARNUNG: FEINDLICHE VERSTÄRKUNG TRIFFT EIN!", 4000)

            elif self.score % 50 == 0 and self.score > 0:
                self.trigger_notification("WARNUNG: FEINDLICHE VERSTÄRKUNG TRIFFT EIN!", 2000)

            if self.score % 10 == 0 and self.score > 0:
                self.current_enemy_speed += config.ENEMY_SPEED_FACTOR

        # Bulets vs Wall
        pygame.sprite.groupcollide(self.bullets, self.obstacles, True, False)

        # Player vs Enemy
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.player.take_damage(config.ENEMY_ATTACK_DMG)
            if not self.player.is_alive:
                self.state = "GAMEOVER"

    def draw_menu(self):
        """Hauptmenü mit Steuerungshinweisen"""
        self.screen.fill(config.COLOR3)
        
        self.ui_manager.draw_screen(self.screen, "306 SCB - Top Down Shooter", "Drücke ENTER zum Starten")

        instructions = [
            "STEUERUNG:",
            "WASD - Bewegen",
            "MAUS - Zielen",
            "LINKSKLICK - Schießen",
            "R - Nachladen",
            "ESC - Pause (im Spiel)/ Beenden"
        ]

        start_y = config.HEIGHT // 2 + 80 
        for i, line in enumerate(instructions):
            
            color = (255, 255, 255) if i == 0 else (200, 200, 200)
            instr_surf = self.small_font.render(line, True, color)
            
            x_pos = config.WIDTH // 2 - instr_surf.get_width() // 2
            y_pos = start_y + (i * 30) 
            
            self.screen.blit(instr_surf, (x_pos, y_pos))

        pygame.display.flip()

    def draw_pause_screen(self):
        self.all_sprites.draw(self.screen)
        
        self.ui_manager.draw_screen(
            self.screen, 
            "PAUSE", 
            "ESC oder ENTER zum Weiterpielen", 
            (50, 50, 50, 150)
        )
        pygame.display.flip()

    def draw_game_over(self):
        self.ui_manager.draw_screen(self.screen, "GAME OVER", f"Score: {self.score} | Drücke R für Neustart", (80, 0, 0, 180))
        pygame.display.flip()

    def draw(self):

        self.screen.fill(config.COLOR3)
    
        self.all_sprites.draw(self.screen)
    
        elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
        self.ui_manager.draw_hud(self.screen, self.player, self.score, elapsed)

        # Notification
        if pygame.time.get_ticks() < self.notification_timer:
            lines = self.notification_text.split('\n')
            
            base_y = 120 
            
            for i, line in enumerate(lines):
                notif_surf = self.small_font.render(line, True, (255, 255, 0))
                
                notif_rect = notif_surf.get_rect(center=(config.WIDTH // 2, base_y + (i * 30)))
                
                bg_rect = notif_rect.inflate(20, 10)
                pygame.draw.rect(self.screen, (0, 0, 0, 150), bg_rect)
                
                self.screen.blit(notif_surf, notif_rect)
    
        pygame.display.flip()

    def spawn_enemy(self):
        spawn_count = config.ENEMY_SPAWN_INCREMENT + (self.score // config.ENEMY_SPAWN_SCORE_STEP)
        
        spawn_count = min(spawn_count, 5)

        for _ in range(spawn_count):
            side = random.randint(0, 3)

            if side == 0:   # Top
                ex, ey = random.randint(0, config.WIDTH), -50
            elif side == 1: # Bottom
                ex, ey = random.randint(0, config.WIDTH), config.HEIGHT + 50
            elif side == 2: # Left
                ex, ey = -50, random.randint(0, config.HEIGHT)
            else:           # Right
                ex, ey = config.WIDTH + 50, random.randint(0, config.HEIGHT)

            new_enemy = Enemy(ex, ey, self.current_enemy_speed)
            self.enemies.add(new_enemy)
            self.all_sprites.add(new_enemy)

    def switch_to_level_two(self):
        if self.current_level_num == 1:
            print("Level 2 beginnt!")
            self.current_level_num = 2
            self.all_sprites.remove(self.obstacles)
            if self.level_exit: self.all_sprites.remove(self.level_exit)
            for e in self.enemies: e.kill()
            for b in self.bullets: b.kill()
            self.load_level(LevelTwo())
            self.player.pos = pygame.Vector2(60, config.HEIGHT // 2)
            self.player.rect.center = self.player.pos

    def trigger_notification(self, text, time):
        duration = time
        self.notification_text = text
        self.notification_timer = pygame.time.get_ticks() + duration

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()