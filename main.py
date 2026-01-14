import pygame

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 820
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shadow Fight Prototype")

# define colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (204, 204, 255)

# Clock that controls FPS
clock = pygame.time.Clock()

# floor settings
FLOOR_Y = 700
FLOOR_HEIGHT = 300

# player settings
speed = 5

# player sizes
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 300
CROUCH_WIDTH = 180
CROUCH_HEIGHT = 210

# Create player rectangles
player1_rect = pygame.Rect(150, FLOOR_Y - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player2_rect = pygame.Rect(600, FLOOR_Y - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Game loop
running = True
while running:
    clock.tick(60)  # ADJUST TO YOUR FRAMERATE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()

    # player 1 movement (WASD)
    if keys[pygame.K_a]:
        player1_rect.x -= speed
    if keys[pygame.K_d]:
        player1_rect.x += speed

    # player 2 movement (arrow keys)
    if keys[pygame.K_LEFT]:
        player2_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player2_rect.x += speed

    # player 1 crouch (S)
    if keys[pygame.K_s]:
        bottom = player1_rect.bottom
        centerx = player1_rect.centerx
        player1_rect.size = (CROUCH_WIDTH, CROUCH_HEIGHT)
        player1_rect.centerx = centerx
        player1_rect.bottom = bottom
    else:
        bottom = player1_rect.bottom
        centerx = player1_rect.centerx
        player1_rect.size = (PLAYER_WIDTH, PLAYER_HEIGHT)
        player1_rect.centerx = centerx
        player1_rect.bottom = bottom

    # player 2 crouch (arrow down)
    if keys[pygame.K_DOWN]:
        bottom = player2_rect.bottom
        centerx = player2_rect.centerx
        player2_rect.size = (CROUCH_WIDTH, CROUCH_HEIGHT)
        player2_rect.centerx = centerx
        player2_rect.bottom = bottom

    else:
        bottom = player2_rect.bottom
        centerx = player2_rect.centerx
        player2_rect.size = (PLAYER_WIDTH, PLAYER_HEIGHT)
        player2_rect.centerx = centerx
        player2_rect.bottom = bottom


    #COLLISION LOGIC TBD
    if player1_rect.colliderect(player2_rect):
        pass

    # lock players to floor
    player1_rect.bottom = FLOOR_Y
    player2_rect.bottom = FLOOR_Y

    # Draw
    display_surface.fill(BACKGROUND_COLOR)  # Set BG color

    # draw floor
    pygame.draw.rect(display_surface, GREEN, (0, FLOOR_Y, SCREEN_WIDTH, FLOOR_HEIGHT))

    # draw players
    pygame.draw.rect(display_surface, BLUE, player1_rect)
    pygame.draw.rect(display_surface, RED, player2_rect)

    pygame.display.update()

pygame.quit()
