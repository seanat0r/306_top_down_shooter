import pygame, sys, random
import config
from src import Player, Projectile, Enemy, LevelOne, LevelTwo

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

# Gruppen helfen dabei, viele Objekte gleichzeitig zu zeichnen/updaten
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()

current_level_obj = LevelOne()
obstacles = current_level_obj.obstacles
level_exit = current_level_obj.exit_portal

all_sprites.add(player)
all_sprites.add(obstacles)
all_sprites.add(level_exit)



last_spawn_time = 0
score = 0

running = True
while running:
    
    dt = clock.tick(60) / 1000.0
    current_time = pygame.time.get_ticks()

    if current_time - last_spawn_time > config.SPAWN_COOLDOWN:
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

        last_spawn_time = current_time

    if pygame.sprite.collide_rect(player, level_exit):
        print("Level Übergang")
        all_sprites.remove(obstacles)
        all_sprites.remove(level_exit)

        for e in enemies: e.kill()
        for b in bullets: b.kill()

        current_level_obj = LevelTwo()
        obstacles = current_level_obj.obstacles
        all_sprites.add(obstacles)

        player.pos = pygame.Vector2(60, config.HEIGHT // 2)
        player.rect.center = player.pos

    # 1. Events (Eingabe)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not player.is_reloading:
                player.reload()
        # Schießen Logik könnte man auch in eine Bullet-Klasse auslagern
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if player.shoot():
                # Hier käme der Schuss-Code hin (Erstellen eines Bullet-Sprites)
                mouse_pos = pygame.mouse.get_pos()
                new_bullet = Projectile(player.rect.center, mouse_pos)

                all_sprites.add(new_bullet)
                bullets.add(new_bullet)
            else:
                print("Keine Munition")

    # 2. Update (Verarbeitung)
    all_sprites.update(player.rect.center, dt, obstacles) 

    hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in hits:
        adding_score = enemy.take_hit(1)
        score += adding_score
        print(f"Score: {score}")
        enemy.upgrade_speed(score)

    pygame.sprite.groupcollide(bullets, obstacles, True, False)
        

    player_hits = pygame.sprite.spritecollide(player, enemies, True)
    for enemy in player_hits:
        player.take_damage(config.ENEMY_ATTACK_DMG)
        print(f"Getroffen! HP übrig: {player.hp}")

        if not player.is_alive:
            print("GAME OVER!")
            running = False
            #! GAME OVER LOGIK

    # 3. Draw (Ausgabe)
    screen.fill(config.COLOR3)
    all_sprites.draw(screen) # Zeichnet ALLES, was in der Gruppe ist
    pygame.display.flip()

pygame.quit()