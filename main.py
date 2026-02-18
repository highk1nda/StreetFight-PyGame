import pygame

from src.modules.fighter.fighter import Fighter

# Initialize pygame
pygame.init()

# screen_info = pygame.display.Info()
# WIDTH = screen_info.current_w
# HEIGHT = screen_info.current_h
WIDTH, HEIGHT = 1000, 600
# Screen setup
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT
FPS = 60
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Skjoldd")

# Load background image
background = pygame.image.load("assets/forest.jpg").convert()  # BG for TEST_ONLY
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
GREEN = (26, 66, 28)

# define knight variables - frame size
KNIGHT_SIZE = 100
KNIGHT_SCALE = 10  # DO NOT INCREASE ABOVE 100
KNIGHT_OFFSET = [40, 37]
KNIGHT_DATA = [KNIGHT_SIZE, KNIGHT_SCALE, KNIGHT_OFFSET]  # 0 - size, 1 - scale, 2 - offset

# Clock that controls FPS
clock = pygame.time.Clock()

# Floor settings
FLOOR_Y = 510
FLOOR_HEIGHT = 200 #Thikness

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
    "assets/Tiny RPG Character Asset Pack v1.03 -Full 20 Characters/Characters(100x100)/Knight/Knight/Knight.png").convert_alpha()  # load the png sheet
# Define amount of animation steps
KNIGHT_ANIMATION_STEPS = [6, 8, 7, 10, 11, 4, 4, 4]  # x,y,z <-> frames per row in sheet
ARM_ORC_ANIMATION_STEPS = [6, 8, 7, 8, 9, 4, 4, 4]

knight_y = FLOOR_Y
werebear = pygame.image.load(
    "assets/Tiny RPG Character Asset Pack v1.03 -Full 20 Characters/Characters(100x100)/Werebear/Werebear/Werebear.png").convert_alpha()
WEREBEAR_ANIMATION_STEPS = [6, 8, 9, 13, 9, 4, 4]
were_test = Fighter(SCREEN_WIDTH - 2*PLAYER_WIDTH, knight_y, KNIGHT_DATA, werebear, WEREBEAR_ANIMATION_STEPS)


# assign knight_test to be part of class Fighter
knight_test = Fighter(1/2*PLAYER_WIDTH, knight_y, KNIGHT_DATA, knight, KNIGHT_ANIMATION_STEPS)

# knight2 = pygame.image.load(
#     "Tiny RPG Character Asset Pack v1.03 -Full 20 Characters/Characters(100x100)/Knight/Knight/Knight.png").convert_alpha()  # load the png sheet
knight2 = pygame.image.load(
    "assets/Tiny RPG Character Asset Pack v1.03 -Full 20 Characters/Characters(100x100)/Armored Orc/Armored Orc/Armored Orc.png").convert_alpha()

knight2_test = Fighter(SCREEN_WIDTH- PLAYER_WIDTH * 2, 10, KNIGHT_DATA, knight2, ARM_ORC_ANIMATION_STEPS)

# PLAYER_1 = {
#     "left": pygame.K_a,
#     "right": pygame.K_d,
#     "jump": pygame.K_w,
#     "attack1": pygame.K_r,
#     "attack2": pygame.K_f,
#     "attack3": pygame.K_v
# }
#
# PLAYER_2 = {
#     "left": pygame.K_LEFT,
#     "right": pygame.K_RIGHT,
#     "jump": pygame.K_UP,
#     "attack1": pygame.K_COMMA,
#     "attack2": pygame.K_PERIOD,
#     "attack3": pygame.K_SLASH
# }

PLAYER_1 = 0
PLAYER_2 = 1
background_music = pygame.mixer.Sound("assets/sfx/Royalty Free Epic Celtic Fantasy Music - Highland Song.mp3")
background_music.set_volume(0.2)
background_music.play()

forest_sfx = pygame.mixer.Sound("assets/sfx/forest-ambience-296528.mp3")
forest_sfx.set_volume(0.1)
forest_sfx.play()

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
    knight_test.move(SCREEN_WIDTH, 610, PLAYER_1) #width, Y position of the player
    were_test.move(SCREEN_WIDTH, 610, PLAYER_2)


    # Update knight
    knight_test.update()
    were_test.update()
    # Draw knight sprite
    knight_test.draw(display_surface)
    were_test.draw(display_surface)
    # Present the rendered frame
    pygame.display.update()

pygame.quit()
