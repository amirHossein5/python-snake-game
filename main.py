import pygame
import sys
import random

pygame.init()

SW, SH = 1300, 700
BLOCK_SIZE = 50
FONT_SIZE = 100

FONT = pygame.font.Font('font.ttf', FONT_SIZE)
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Snake game')


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
        if self.dead:
            self.__init__()
            self.dead = False
            global apple
            apple = Apple()

        for i, rect in enumerate(self.body):
            if i == len(self.body) - 1:
                rect.x = self.head.x
                rect.y = self.head.y
                continue

            rect.x = self.body[i+1].x
            rect.y = self.body[i+1].y

        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE

    def chech_death(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True

        if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
            self.dead = True

    def draw(self):
        pygame.draw.rect(screen, "blue", self.head)

        for square in self.body:
            pygame.draw.rect(screen, "green", square)


class Apple:
    def __init__(self):
        self.x = random.randint(0, SW) // BLOCK_SIZE * BLOCK_SIZE
        self.y = random.randint(0, SH) // BLOCK_SIZE * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self):
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

    screen.fill('black')
    draw_grid()
    snake.chech_death()
    snake.update()
    snake.draw()
    apple.draw()

    score = FONT.render(f"{len(snake.body)}", True, "white")
    screen.blit(score, score.get_rect(center=(SW-FONT_SIZE, SH-FONT_SIZE)))

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(
            snake.body[-1].x, snake.body[-1].y, BLOCK_SIZE, BLOCK_SIZE)
        )
        apple = Apple()

    pygame.display.update()
    pygame.time.Clock().tick(10)
