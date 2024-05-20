import pygame
import sys
import random

pygame.init()

SW, SH = 1300, 700
BLOCK_SIZE = 20

# FONT = pygame.font.Font('font.ttf', 100)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Snake!')
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(
            self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE
        )]
        self.dead = False

    def update(self):
        for i, rect in enumerate(self.body):
            if i == len(self.body) - 1:
                rect.x = self.head.x
                rect.y = self.head.y
                continue

            rect.x = self.body[i+1].x
            rect.y = self.body[i+1].y

        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE


class Apple:
    def __init__(self):
        self.x = random.randint(0, SW) // BLOCK_SIZE * BLOCK_SIZE
        self.y = random.randint(0, SH) // BLOCK_SIZE * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)


def draw_grid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3b', rect, 1)


draw_grid()
snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_j, pygame.K_s, pygame.K_DOWN]:
                snake.xdir = 0
                snake.ydir = 1
            elif event.key in [pygame.K_k, pygame.K_w, pygame.K_UP]:
                snake.xdir = 0
                snake.ydir = -1
            elif event.key in [pygame.K_h, pygame.K_a, pygame.K_LEFT]:
                snake.xdir = -1
                snake.ydir = 0
            elif event.key in [pygame.K_l, pygame.K_d, pygame.K_RIGHT]:
                snake.xdir = 1
                snake.ydir = 0

    snake.update()
    screen.fill('black')
    draw_grid()
    apple.update()

    pygame.draw.rect(screen, "blue", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(
            snake.head.x, snake.head.y, BLOCK_SIZE, BLOCK_SIZE)
        )
        apple = Apple()

    pygame.display.update()
    clock.tick(30)
