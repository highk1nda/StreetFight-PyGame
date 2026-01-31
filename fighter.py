import pygame


class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect(x, y, 200, 200)
        self.vel_y = 0

    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        FLOOR_HEIGHT = 100

        # Key presses
        key = pygame.key.get_pressed()
        #
        # EDIT FOR EACH PLAYER
        # SPLIT IN TWO CLASS INSTANCES
        #
        # MOVEMENT BINDS WASD
        if key[pygame.K_d]:  # RIGHT
            dx += SPEED
        if key[pygame.K_a]:  # LEFT
            dx -= SPEED
        # jumping
        if key[pygame.K_w]:  # UP
            self.vel_y -= SPEED

        # MOVEMENT BINDS ARROWS
        if key[pygame.K_RIGHT]:  # RIGHT
            dx += SPEED
        if key[pygame.K_LEFT]:  # LEFT
            dx -= SPEED
        # jumping
        if key[pygame.K_UP]:  # UP
            self.vel_y -= SPEED
        #

        # gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # is player on screen
        if self.rect.left + dx < 0:
            dx -= self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right
        if self.rect.bottom + dy > SCREEN_HEIGHT - FLOOR_HEIGHT:
            self.vel_y = 0
            dy = SCREEN_HEIGHT - FLOOR_HEIGHT - self.rect.bottom
        if self.rect.top + dy > SCREEN_HEIGHT:
            self.vel_y = 0
        if self.rect.top + dy < 0:
            self.vel_y = 0

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (222, 110, 0), self.rect)

#     # Player 1 crouch (S)
#     if keys[pygame.K_s]:
#         bottom = player1_rect.bottom
#         centerx = player1_rect.centerx
#         player1_rect.size = (CROUCH_WIDTH, CROUCH_HEIGHT)
#         player1_rect.centerx = centerx
#         player1_rect.bottom = bottom
#     else:
#         bottom = player1_rect.bottom
#         centerx = player1_rect.centerx
#         player1_rect.size = (PLAYER_WIDTH, PLAYER_HEIGHT)
#         player1_rect.centerx = centerx
#         player1_rect.bottom = bottom
