import pygame, sys, math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

COLOR1 = (255, 255, 255)
COLOR2 = (255, 255, 255)
COLOR3 = (0, 0, 0)

player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
player_speed = 4
bullets = []
bullet_speed = 10

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            dir_vec = pygame.Vector2(mx, my) - player_pos
            if dir_vec.length() != 0:
                dir_vec = dir_vec.normalize()
            bullets.append({
                "pos": player_pos.copy(),
                "dir": dir_vec
            })

    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0, 0)
    if keys[pygame.K_w]:
        move.y -= 1
    if keys[pygame.K_s]:
        move.y += 1
    if keys[pygame.K_a]:
        move.x -= 1
    if keys[pygame.K_d]:
        move.x += 1
    if move.length() != 0:
        move = move.normalize() * player_speed
    player_pos += move

    for b in bullets:
        b["pos"] += b["dir"] * bullet_speed
    bullets = [b for b in bullets if 0 <= b["pos"].x <= WIDTH and 0 <= b["pos"].y <= HEIGHT]

    screen.fill(COLOR3)
    pygame.draw.circle(screen, COLOR1, player_pos, 15)
    for b in bullets:
        pygame.draw.circle(screen, COLOR2, (int(b["pos"].x), int(b["pos"].y)), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()