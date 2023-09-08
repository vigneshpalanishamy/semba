import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lion Adventure")

# Load images
lion = pygame.image.load("lion.gif")
cave = pygame.image.load("cave.jpg")

# Get lion's initial position
lion_x = 50
lion_y = 450

# Main game loop
running = True
moving = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move lion if arrow keys are pressed
    if keys[pygame.K_UP]:
        lion_y -= 5
        moving = True
    if keys[pygame.K_DOWN]:
        lion_y += 5
        moving = True
    if keys[pygame.K_LEFT]:
        lion_x -= 5
        moving = True
    if keys[pygame.K_RIGHT]:
        lion_x += 5
        moving = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw images
    screen.blit(lion, (lion_x, lion_y))
    screen.blit(cave, (600, 375))

    pygame.display.flip()

    if not any(keys):
        moving = False

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
