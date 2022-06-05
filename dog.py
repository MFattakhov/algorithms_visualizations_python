import pygame
import sys
import numpy as np
import random
from funcs import draw, save

pygame.init()


def game():
    clock = pygame.time.Clock()

    fps = 2
    colors = ['black', 'brown', 'white', 'blue']
    n = 45
    size = width, height = n * 10, n * 10
    screen = pygame.display.set_mode(size)

    matrix = [[np.random.choice([0, 2], p=[.6, .4]) for _ in range(n)] for _ in range(n)]

    x, y = n // 2, n // 2
    matrix[x][y] = 0

    while x > 0 and x < n - 1 and y > 0 and y < n - 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        matrix[x][y] = 1
        draw(screen, clock, fps, matrix, colors)
        if matrix[x - 1][y] + matrix[x + 1][y] + matrix[x][y - 1] + matrix[x][y + 1] >= 7:
            x_new, y_new = random.choice([(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 0])
            matrix[x][y] = 3
            save(screen, clock, fps * 5, matrix, colors, x * 10, y * 10, x_new * 10, y_new * 10, n)
            matrix[x][y] = 1
            x, y = x_new, y_new
        elif matrix[x - 1][y] == 0:
            x -= 1
        elif matrix[x + 1][y] == 0:
            x += 1
        elif matrix[x][y - 1] == 0:
            y -= 1
        elif matrix[x][y + 1] == 0:
            y += 1
        else:
            t = 2
            while t == 2:
                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                t = matrix[x + dx][y + dy]
            x += dx
            y += dy
    matrix[x][y] = 1
    draw(screen, clock, fps, matrix, colors)



if __name__ == '__main__':
    game()

pygame.quit()
sys.exit()
