import pygame, sys
import config
from src import Player, Projectile

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

# Gruppen helfen dabei, viele Objekte gleichzeitig zu zeichnen/updaten
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    # 1. Events (Eingabe)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Schießen Logik könnte man auch in eine Bullet-Klasse auslagern
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Hier käme der Schuss-Code hin (Erstellen eines Bullet-Sprites)
            mouse_pos = pygame.mouse.get_pos()
            new_bullet = Projectile(player.rect.center, mouse_pos)

            all_sprites.add(new_bullet)
            bullets.add(new_bullet)
            pass

    # 2. Update (Verarbeitung)
    all_sprites.update() 

    # 3. Draw (Ausgabe)
    screen.fill(config.COLOR3)
    all_sprites.draw(screen) # Zeichnet ALLES, was in der Gruppe ist
    pygame.display.flip()

pygame.quit()