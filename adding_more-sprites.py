import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

clock = pygame.time.Clock()

player_size = 50
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, player_size, player_size)

enemy_size = 50
enemies = [pygame.Rect(random.randint(0, WIDTH - enemy_size),
                       random.randint(0, HEIGHT - enemy_size),
                       enemy_size, enemy_size) for _ in range(7)]

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
        player.x += 5
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player_size:
        player.y += 5

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT - enemy_size)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
