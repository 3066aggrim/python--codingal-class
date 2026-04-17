import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Circle and Rectangle")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

window.fill(WHITE)

pygame.draw.circle(window, GREEN, (200, 150), 50)
pygame.draw.circle(window, BLACK, (400, 150), 50, 3)

pygame.draw.rect(window, BLUE, (150, 300, 120, 80))
pygame.draw.rect(window, BLACK, (350, 300, 120, 80), 3)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
window.fill(WHITE)

# draw circles
pygame.draw.circle(window, GREEN, (200, 150), 50)
pygame.draw.circle(window, BLACK, (400, 150), 50, 3)

# draw rectangles
pygame.draw.rect(window, BLUE, (150, 300, 120, 80))
pygame.draw.rect(window, BLACK, (350, 300, 120, 80), 3)

# update display
pygame.display.update()

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
