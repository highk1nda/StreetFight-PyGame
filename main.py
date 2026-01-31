import pygame
from fighter import Fighter

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 1520
SCREEN_HEIGHT = 820
FPS = 60
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Medieval Mayhem")

# Load background image
background = pygame.image.load("forest.jpg").convert()  # BG for TEST_ONLY
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
GREEN = (26, 66, 28)

# Clock that controls FPS
clock = pygame.time.Clock()

# Floor settings
FLOOR_Y = 720
FLOOR_HEIGHT = 100

# Player settings
speed = 5

# Player sizes
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 270
CROUCH_WIDTH = 180
CROUCH_HEIGHT = 210

# Create player rectangles
player1_rect = pygame.Rect(150, FLOOR_Y - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player2_rect = pygame.Rect(600, FLOOR_Y - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Load spritesheets
knight = pygame.image.load(
    "Tiny RPG Character Asset Pack v1.03 -Full 20 Characters/Characters(100x100)/Knight/Knight/Knight.png").convert_alpha()  # load the png sheet
# Define amount of animation steps
KNIGHT_ANIMATION_STEPS = [6, 8, 7, 10, 11, 4, 4, 4]  # x,y,z <-> frames per row in sheet
# assign knight_test to be part of class Fighter
knight_test = Fighter(PLAYER_WIDTH, FLOOR_Y - PLAYER_HEIGHT)
# Game loop
running = True
while running:
    clock.tick(FPS)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Key input
    keys = pygame.key.get_pressed()

    # RENDERING
    # Draw background
    display_surface.blit(background, (0, 0))
    # Draw floor
    pygame.draw.rect(display_surface, GREEN, (0, FLOOR_Y, SCREEN_WIDTH, FLOOR_HEIGHT))

    # GAME LOGIC
    # Update knight movement and state
    knight_test.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Draw knight sprite
    knight_test.draw(display_surface)
    # Present the rendered frame
    pygame.display.update()

pygame.quit()
