import pygame
import sys
import random
from funcs import draw, gameover
from collections import deque

pygame.init()


def game():
    clock = pygame.time.Clock()

    fps = 8
    colors = ['white', 'green', 'red']
    n = 20
    size = width, height = n * 10, n * 10
    screen = pygame.display.set_mode(size)

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    x, y = n // 2, n // 2
    snake = deque([(x, y)])
    velocity = (1, 0)
    velocities = {
        pygame.K_UP: (-1, 0),
        pygame.K_DOWN: (1, 0),
        pygame.K_LEFT: (0, -1),
        pygame.K_RIGHT: (0, 1)
    }

    apple_x, apple_y = random.choice([(i, j) for i in range(1, n - 1) for j in range(1, n - 1) if matrix[i][j] == 0])
    matrix[apple_x][apple_y] = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                '''match event.key:
                    case pygame.K_UP | pygame.K_DOWN if velocity[0] == 0:
                        velocity = velocities[event.key]
                    case pygame.K_RIGHT | pygame.K_LEFT if velocity[1] == 0:
                        velocity = velocities[event.key]'''
                if event.key in [pygame.K_UP, pygame.K_DOWN] and velocity[0] == 0:
                    velocity = velocities[event.key]
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT] and velocity[1] == 0:
                    velocity = velocities[event.key]

        draw(screen, clock, fps, matrix, colors)
        snake.appendleft((snake[0][0] + velocity[0], snake[0][1] + velocity[1]))
        x, y = snake[0]
        x_0, y_0 = snake.pop()
        matrix[x_0][y_0] = 0
        if x > n - 1 or y > n - 1 or y < 0 or x < 0:
            gameover(screen)
        if matrix[x][y] == 1:
            gameover(screen)
        if matrix[x][y] == 2:
            snake.append(snake[-1])
            apple_x, apple_y = random.choice([(i, j) for i in range(1, n - 1) for j in range(1, n - 1) if matrix[i][j] == 0])
            matrix[apple_x][apple_y] = 2
        matrix[x][y] = 1


if __name__ == '__main__':
    game()

pygame.quit()
sys.exit()
