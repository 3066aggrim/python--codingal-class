import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites")

BLUE = pygame.Color('blue')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')


class AutoSprite(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - w)
        self.rect.y = random.randint(0, HEIGHT - h)
        self.vel = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vel[0] *= -1
            self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE]))

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vel[1] *= -1
            self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE]))


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.color = color

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
        if keys[pygame.K_UP]:
            self.rect.y -= 4
        if keys[pygame.K_DOWN]:
            self.rect.y += 4

        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

        if self.rect.left == 0:
            self.image.fill(BLUE)
        elif self.rect.right == WIDTH:
            self.image.fill(YELLOW)
        elif self.rect.top == 0:
            self.image.fill(RED)
        elif self.rect.bottom == HEIGHT:
            self.image.fill(GREEN)
        else:
            self.image.fill(WHITE)


all_sprites = pygame.sprite.Group()

auto = AutoSprite(WHITE, 30, 30)
player = PlayerSprite(WHITE, 60, 60)

all_sprites.add(auto)
all_sprites.add(player)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
