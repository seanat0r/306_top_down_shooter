import pygame, sys, random
import config
from src import Player, Projectile, Enemy

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

# Gruppen helfen dabei, viele Objekte gleichzeitig zu zeichnen/updaten
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

running = True
while running:
    dt = clock.tick(60) / 1000.0
    current_time = pygame.time.get_ticks()

    if current_time - config.SPWAN_TIMER > config.SPWAN_TIMER:
        side = random.randint(0, 3)
        if side == 0:
            ex, ey = random.randint(0, config.WIDTH), -50
        elif side == 1:
            ex, ey = random.randint(0, config.WIDTH), config.HEIGHT + 50
        elif side == 2:
            ex, ey = -50, random.randint(0, config.HEIGHT) 
        else:
            ex, ey = config.WIDTH + 50, random.randint(0, config.HEIGHT)

        new_enemy = Enemy(ex, ey)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

        spawn_timer = current_time

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

    hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in hits:
        enemy.take_hit(1)

    player_hits = pygame.sprite.spritecollide(player, enemies, True)
    for enemy in player_hits:
        player.take_damage(config.ENEMY_ATTACK_DMG)
        print(f"Getroffen! HP übrig: {player.hp}")

        if not player.is_alive:
            print("GAME OVER!")
            #! GAME OVER LOGIK

    # 3. Draw (Ausgabe)
    screen.fill(config.COLOR3)
    all_sprites.draw(screen) # Zeichnet ALLES, was in der Gruppe ist
    pygame.display.flip()

pygame.quit()