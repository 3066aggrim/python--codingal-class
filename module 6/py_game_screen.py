# Import Necessary Libraries
import pygame

# initialize required module
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((1000, 500))

# Create a loop to run till the game is quit by the user
done = False

while not done:

    # clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
# make the changes visible
    pygame.display.flip()
