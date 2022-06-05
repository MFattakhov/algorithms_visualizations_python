import pygame
import random
import sys

def draw(screen, clock, fps, matrix, colors):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            pygame.draw.rect(screen, colors[matrix[i][j]], (j * 10, i * 10, 10, 10))

    pygame.display.flip()
    clock.tick(fps)


def save(screen, clock, fps, matrix, colors, from_y, from_x, to_y, to_x, n):
    r = random.randint(0, 4 * n - 1)
    r1, r2 = r // n, r % n
    if r1 == 0:
        x_0, y_0 = r2 * 10, 0
    elif r1 == 1:
        x_0, y_0 = (n - 1) * 10, r2 * 10
    elif r1 == 2:
        x_0, y_0 = r2 * 10, (n - 1) * 10
    else:
        x_0, y_0 = 0, r2 * 10
    dx = (from_x - x_0) / 20
    dy = (from_y - y_0) / 20
    while (x_0, y_0) != (from_x, from_y):
        if abs(from_x - x_0) + abs(from_y - y_0) < 5:
            x_0, y_0 = from_x, from_y
            break
        x_0 += dx
        y_0 += dy
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                pygame.draw.rect(screen, colors[matrix[i][j]], (j * 10, i * 10, 10, 10))
        pygame.draw.rect(screen, 'red', (int(x_0), int(y_0), 10, 10))
        pygame.display.flip()
        clock.tick(fps)
    matrix[from_y // 10][from_x // 10] = 1
    dx = (to_x - x_0) / 20
    dy = (to_y - y_0) / 20
    while (x_0, y_0) != (to_x, to_y):
        if abs(to_x - x_0) + abs(to_y - y_0) < 5:
            x_0, y_0 = to_x, to_y
            break
        x_0 += dx
        y_0 += dy
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                pygame.draw.rect(screen, colors[matrix[i][j]], (j * 10, i * 10, 10, 10))
        pygame.draw.rect(screen, 'red', (int(x_0), int(y_0), 10, 10))
        pygame.display.flip()
        clock.tick(fps)


def gameover(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screen.fill('black')
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        label = myfont.render("GAME OVER", 1, 'white')
        screen.blit(label, (0, 0))
        pygame.display.flip()
