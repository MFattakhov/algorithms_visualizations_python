import pygame
import sys
import numpy as np
import random
from funcs import draw
import heapq


pygame.init()


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def neighbours(x, y, matrix):
    rez = []
    for x_, y_ in [(_, __) for _ in range(x - 1, x + 2) for __ in range(y - 1, y + 2)]:
        if len(matrix[0]) > x_ >= 0 and \
           len(matrix) > y_ >= 0 and abs(x_ - x) + abs(y_ - y) == 1 and \
           matrix[y_][x_] != 0:
            rez.append((x_, y_))
    return rez


def heuristic(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def find_path(start, end, matrix):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            path = []
            path_i = end
            while path_i:
                path.append(path_i)
                path_i = came_from[path_i]
            return path
        
        new_cost = cost_so_far[current] + 2
        for next in neighbours(*current, matrix):
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, end)
                frontier.put(next, priority)
                came_from[next] = current


def main():
    clock = pygame.time.Clock()

    fps = 30
    colors = ['black', 'white', 'blue']
    n = 45
    size = width, height = n * 10, n * 10
    screen = pygame.display.set_mode(size)

    matrix = [[np.random.choice([1, 0], p=[.8, .2]) for _ in range(n)] for _ in range(n)]

    start = (random.randint(0, n - 1), random.randint(0, n - 1))
    end = None
    while True:
        matrix[start[1]][start[0]] = 2
        draw(screen, clock, fps, matrix, colors)
        if end:
            matrix[end[1]][end[0]] = 2
            path = find_path(start, end, matrix)
            for path_i in reversed(path + [start]):
                matrix[path_i[1]][path_i[0]] = 2
                draw(screen, clock, fps, matrix, colors)
            for path_i in reversed(path):
                if path_i != end:
                    matrix[path_i[1]][path_i[0]] = 1
                    draw(screen, clock, fps, matrix, colors)
            start = end
            end = None
            for y in range(n):
                for x in range(n):
                    if matrix[y][x] == 2:
                        matrix[y][x] = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                end = (pos[0] // 10, pos[1] // 10)


if __name__ == '__main__':
    main()

pygame.quit()
sys.exit()