import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500


display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding Kadita and Background ML Image')

background_image = pygame.image.load('background.png').convert()
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

ml_image = pygame.image.load('mobile_legends.png').convert_alpha()
ml_image = pygame.transform.scale(ml_image, (200, 200))
ml_rect = ml_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

# Text
font = pygame.font.Font(None, 36)
text = font.render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(ml_image, ml_rect)

        display_surface.blit(text, text_rect)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    game_loop()
