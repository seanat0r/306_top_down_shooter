import pygame
import random
import config
from src import Player, Projectile, Enemy, LevelOne, LevelTwo

class Game:
    def __init__(self):
        # Initialisierung
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("Top-Down Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Font für HUD (Vorbereitung)
        self.font = pygame.font.SysFont("Arial", 48)    
        self.small_font = pygame.font.SysFont("Arial", 24)

        self.state = "MENU"

    def new(self):
        """Startet ein neues Spiel oder resettet eine Runde"""
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # Player Setup
        self.player = Player()
        self.all_sprites.add(self.player)
        
        # Level Management
        self.current_level_num = 1
        self.load_level(LevelOne())
        
        # Statistiken
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.last_spawn_time = 0
        self.game_over = False

    def load_level(self, level_obj):
        """Hilfsfunktion zum Wechseln der Level-Daten"""
        self.current_level_obj = level_obj
        self.obstacles = self.current_level_obj.obstacles
        self.level_exit = self.current_level_obj.exit_portal
        
        # Wir fügen die neuen Hindernisse und den Ausgang zur Gruppe hinzu
        self.all_sprites.add(self.obstacles)
        if self.level_exit:
            self.all_sprites.add(self.level_exit)

    def run(self):
        """Die Hauptschleife des Spiels"""
        while self.running:
            self.dt = self.clock.tick(60) / 1000.0
            self.events()

            match self.state:
                case "MENU":
                    self.draw_menu()

                case "PLAYING":
                    self.update()
                    self.draw()

                case "GAMEOVER":
                    self.draw_game_over()

    def events(self):
        """Input Handling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            match self.state:
                case "MENU":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN: # ENTER zum Starten
                            self.new()
                            self.state = "PLAYING"
            
                case "PLAYING":
                    if not self.game_over:
                        # Manueller Reload
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
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r: # R für Neustart
                            self.state = "MENU"

    def draw_menu(self):
        self.screen.fill(config.COLOR3)
        title_surf = self.font.render("MEIN SHOOTER", True, (255, 255, 255))
        start_surf = self.small_font.render("Drücke ENTER zum Starten", True, (200, 200, 200))
        
        self.screen.blit(title_surf, (config.WIDTH//2 - 150, config.HEIGHT//2 - 50))
        self.screen.blit(start_surf, (config.WIDTH//2 - 130, config.HEIGHT//2 + 50))
        pygame.display.flip()

    def draw_game_over(self):
        self.screen.fill((50, 0, 0)) # Dunkles Rot
        go_surf = self.font.render("GAME OVER", True, config.RED)
        score_surf = self.small_font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_surf = self.small_font.render("Drücke R für das Menü", True, (200, 200, 200))

        self.screen.blit(go_surf, (config.WIDTH//2 - 120, config.HEIGHT//2 - 80))
        self.screen.blit(score_surf, (config.WIDTH//2 - 80, config.HEIGHT//2))
        self.screen.blit(restart_surf, (config.WIDTH//2 - 100, config.HEIGHT//2 + 80))
        pygame.display.flip()

    def update(self):
        """Spiellogik"""
        current_time = pygame.time.get_ticks()
        
        # 1. Spawning
        if current_time - self.last_spawn_time > config.SPAWN_COOLDOWN:
            self.spawn_enemy()
            self.last_spawn_time = current_time

        # 2. Sprite Updates
        # Wir geben Player-Position, dt und Obstacles an alle Sprites weiter
        self.all_sprites.update(self.player.rect.center, self.dt, self.obstacles)

        # 3. Kollisionen prüfen
        self.check_collisions()

        # 4. Level Übergang prüfen
        if self.level_exit is not None:
            if pygame.sprite.collide_rect(self.player, self.level_exit):
                self.switch_to_level_two()

    def check_collisions(self):
        # Gegner vs Kugeln
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for enemy in hits:
            adding_score = enemy.take_hit(1)
            self.score += adding_score
            # Dynamische Schwierigkeit (GDD 1.3)
            if self.score % 10 == 0:
                config.ENEMY_SPEED += config.ENEMY_SPEED_FACTOR

        # Kugeln vs Hindernisse
        pygame.sprite.groupcollide(self.bullets, self.obstacles, True, False)

        # Spieler vs Gegner
        player_hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for enemy in player_hits:
            self.player.take_damage(config.ENEMY_ATTACK_DMG)
            if not self.player.is_alive:
                print(f"GAME OVER! Score: {self.score}")
                self.game_over = True

    def spawn_enemy(self):
        side = random.randint(0, 3)
        if side == 0: ex, ey = random.randint(0, config.WIDTH), -50
        elif side == 1: ex, ey = random.randint(0, config.WIDTH), config.HEIGHT + 50
        elif side == 2: ex, ey = -50, random.randint(0, config.HEIGHT)
        else: ex, ey = config.WIDTH + 50, random.randint(0, config.HEIGHT)

        new_enemy = Enemy(ex, ey)
        self.enemies.add(new_enemy)
        self.all_sprites.add(new_enemy)

    def switch_to_level_two(self):
        if self.current_level_num == 1:
            print("Wechsle zu Level 2")
            self.current_level_num = 2
            
            # Aufräumen
            self.all_sprites.remove(self.obstacles)
            self.all_sprites.remove(self.level_exit)
            for e in self.enemies: e.kill()
            for b in self.bullets: b.kill()
            
            # Neues Level laden
            self.load_level(LevelTwo())
            
            # Spieler zurücksetzen
            self.player.pos = pygame.Vector2(60, config.HEIGHT // 2)
            self.player.rect.center = self.player.pos

    def draw(self):
        # Hintergrund
        self.screen.fill(config.COLOR3)
        
        # Alle Sprites zeichnen
        self.all_sprites.draw(self.screen)
        
        # (Platzhalter für HUD Funktion)
        self.draw_debug_info()
        
        pygame.display.flip()

    def draw_debug_info(self):
        """Erste Textanzeigen (Vorbote des HUD)"""
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        info_text = f"Score: {self.score} | HP: {self.player.hp} | Time: {elapsed_time}s | Ammo: {self.player.ammo}"
        text_surf = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(text_surf, (10, 10))
        
        if self.game_over:
            go_text = self.font.render("GAME OVER - Drücke Esc zum Beenden", True, config.RED)
            self.screen.blit(go_text, (config.WIDTH//2 - 150, config.HEIGHT//2))

if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
    pygame.quit()