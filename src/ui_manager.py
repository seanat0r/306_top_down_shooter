import pygame
import config

class UIManager:
    def __init__(self):
        # Fonts laden
        self.font_main = pygame.font.SysFont("Arial", 48, bold=True)
        self.font_hud = pygame.font.SysFont("Arial", 22, bold=True)
        
        
        self.COLOR_HP = config.COLOR_HP
        self.COLOR_AMMO = config.COLOR_AMMO
        self.COLOR_RELOAD = config.COLOR_RELOAD
        self.COLOR_TEXT = config.COLOR_TEXT

    def draw_hud(self, screen, player, score, elapsed_time):
        """Zeichnet das HUD während des Spiels"""
        
        # --- 1. Lebensanzeige (Oben Links) ---
        heart_size = 30 # Die ungefähre Größe des Herzens
        for i in range(player.hp):
            # Berechne die Position für jedes Herz
            heart_x = 20 + (i * 40)
            heart_y = 20
            # Rufe die Hilfsfunktion zum Zeichnen auf
            self._draw_heart_shape(screen, heart_x, heart_y, heart_size)

        # --- 2. Score & Zeit (Unter HP) ---
        score_surf = self.font_hud.render(f"SCORE: {score:04d}", True, self.COLOR_TEXT)
        screen.blit(score_surf, (20, 45))

        circle_radius = 12
        padding = 10
        # Startposition (unten rechts)
        start_x = config.WIDTH - 40
        start_y = config.HEIGHT - 40
        
        # Ammo-Ratio berechnen
        ammo_ratio = player.ammo / player.max_ammo if player.max_ammo > 0 else 0
        thresholds = [0.25, 0.50, 0.75, 1.0]

        for i in range(4):
            # Wir zeichnen von unten (Index 0) nach oben (Index 3)
            pos_y = start_y - (i * (circle_radius * 2 + padding))
            
            # Hintergrund/Rahmen des Kreises
            pygame.draw.circle(screen, (50, 50, 50), (start_x, pos_y), circle_radius)
            
            # Füllung prüfen
            # Kreis leuchtet, wenn die Munition den Schwellenwert erreicht
            if ammo_ratio >= thresholds[i]:
                color = self.COLOR_AMMO if not player.is_reloading else self.COLOR_RELOAD
                pygame.draw.circle(screen, color, (start_x, pos_y), circle_radius - 2)
            
            # Weißer Rand für die Optik
            pygame.draw.circle(screen, self.COLOR_TEXT, (start_x, pos_y), circle_radius, 2)

        # Kleiner Text unter/über den Kreisen
        ammo_label = self.font_hud.render(f"{player.ammo}", True, self.COLOR_TEXT)
        screen.blit(ammo_label, (start_x - 10, start_y + 15))

    def draw_screen(self, screen, title, subtitle, bg_color=(0, 0, 0, 150)):
        """Universal-Methode für Menü und Game Over"""
        # Overlay für bessere Lesbarkeit
        overlay = pygame.Surface((config.WIDTH, config.HEIGHT), pygame.SRCALPHA)
        overlay.fill(bg_color)
        screen.blit(overlay, (0, 0))

        # Texte rendern
        title_surf = self.font_main.render(title, True, self.COLOR_TEXT)
        sub_surf = self.font_hud.render(subtitle, True, (200, 200, 200))

        # Zentrieren
        title_rect = title_surf.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 - 40))
        sub_rect = sub_surf.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 + 40))

        screen.blit(title_surf, title_rect)
        screen.blit(sub_surf, sub_rect)

    def _draw_heart_shape(self, screen, x, y, size):
        """
        Verbesserte Herzform: Breiteres Dreieck, höhere Position 
        und saubere Überlappung ohne interne schwarze Linien.
        """
        # 1. Alles ein Stück nach oben verschieben (y - 8)
        y_adj = y - 8
        
        # Radius für die "Schultern" (ca. 35% der Größe für volle Rundungen)
        circle_radius = int(size * 0.35)
        
        left_center = (x + circle_radius, y_adj + circle_radius)
        right_center = (x + size - circle_radius, y_adj + circle_radius)

        # --- FÜLLUNG (Zuerst alles Rot zeichnen) ---
        pygame.draw.circle(screen, self.COLOR_HP, left_center, circle_radius)
        pygame.draw.circle(screen, self.COLOR_HP, right_center, circle_radius)

        # Das Dreieck ist jetzt "dicker" (volle Breite von x bis x+size)
        # Es startet höher (direkt auf der Mittellinie der Kreise)
        triangle_points = [
            (x, y_adj + circle_radius),              # Ganz links außen
            (x + size, y_adj + circle_radius),       # Ganz rechts außen
            (x + size // 2, y_adj + size)            # Spitze unten
        ]
        pygame.draw.polygon(screen, self.COLOR_HP, triangle_points)

