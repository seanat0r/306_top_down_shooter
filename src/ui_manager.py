import pygame
from . import config

class UIManager:
    def __init__(self):
        # Fonts loading
        self.font_main = pygame.font.SysFont("Arial", 48, bold=True)
        self.font_hud = pygame.font.SysFont("Arial", 22, bold=True)
        
        
        self.COLOR_HP = config.COLOR_HP
        self.COLOR_AMMO = config.COLOR_AMMO
        self.COLOR_RELOAD = config.COLOR_RELOAD
        self.COLOR_TEXT = config.COLOR_TEXT

    def draw_hud(self, screen, player, score, elapsed_time):
        """Zeichnet das HUD während des Spiels"""
        
        # --- 1. Life (Top Left) ---
        heart_size = 30 
        for i in range(player.hp):
            
            heart_x = 20 + (i * 40)
            heart_y = 20
           
            self._draw_heart_shape(screen, heart_x, heart_y, heart_size)

        # --- 2. Score (Below HP) ---
        score_surf = self.font_hud.render(f"SCORE: {score:04d}", True, self.COLOR_TEXT)
        screen.blit(score_surf, (20, 45))

        circle_radius = 12
        padding = 10
        
        start_x = config.WIDTH - 40
        start_y = config.HEIGHT - 40
        
        # -- 3. Ammo (Bottom Right) ---
        ammo_ratio = player.ammo / player.max_ammo if player.max_ammo > 0 else 0
        thresholds = [0.25, 0.50, 0.75, 1.0]

        for i in range(4):
            pos_y = start_y - (i * (circle_radius * 2 + padding))

            pygame.draw.circle(screen, (50, 50, 50), (start_x, pos_y), circle_radius)

            if ammo_ratio >= thresholds[i]:
                color = self.COLOR_AMMO if not player.is_reloading else self.COLOR_RELOAD
                pygame.draw.circle(screen, color, (start_x, pos_y), circle_radius - 2)
            
            pygame.draw.circle(screen, self.COLOR_TEXT, (start_x, pos_y), circle_radius, 2)

        ammo_label = self.font_hud.render(f"{player.ammo}", True, self.COLOR_TEXT)
        screen.blit(ammo_label, (start_x - 10, start_y + 15))

    def draw_screen(self, screen, title, subtitle, bg_color=(0, 0, 0, 150)):
        overlay = pygame.Surface((config.WIDTH, config.HEIGHT), pygame.SRCALPHA)
        overlay.fill(bg_color)
        screen.blit(overlay, (0, 0))

        title_surf = self.font_main.render(title, True, self.COLOR_TEXT)
        sub_surf = self.font_hud.render(subtitle, True, (200, 200, 200))

        title_rect = title_surf.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 - 40))
        sub_rect = sub_surf.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 + 40))

        screen.blit(title_surf, title_rect)
        screen.blit(sub_surf, sub_rect)

    def _draw_heart_shape(self, screen, x, y, size):
        y_adj = y - 8

        circle_radius = int(size * 0.35)
        
        left_center = (x + circle_radius, y_adj + circle_radius)
        right_center = (x + size - circle_radius, y_adj + circle_radius)
        pygame.draw.circle(screen, self.COLOR_HP, left_center, circle_radius)
        pygame.draw.circle(screen, self.COLOR_HP, right_center, circle_radius)

        triangle_points = [
            (x, y_adj + circle_radius),              
            (x + size, y_adj + circle_radius),      
            (x + size // 2, y_adj + size)            
        ]
        pygame.draw.polygon(screen, self.COLOR_HP, triangle_points)

