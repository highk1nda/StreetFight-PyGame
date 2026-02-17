import pygame


class Fighter():
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = False
        self.animation_list = self.load_images(sprite_sheet,
                                               animation_steps)  # Load in the sheet straight away. List of lists of animations
        self.action = 0  # 0 - IDLE 1 - Walk
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x, y, 200, 200)
        self.vel_y = 0
        self.running = False
        self.jumping = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.hit = False
        self.death = False
        self.walk_sound = pygame.mixer.Sound(
            "assets/sfx/knight-right-footstep-on-gravel-4-with-chainmail-101937.mp3"
        )
        self.sword_attack1_sound = pygame.mixer.Sound("assets/sfx/sword_sfx/sword-slice-393847.mp3")
        self.sword_attack2_sound = pygame.mixer.Sound(
            "assets/sfx/sword_sfx/sword-slashing-game-sound-effect-1-379228.mp3")
        self.sword_attack3_sound = pygame.mixer.Sound("assets/sfx/sword_sfx/short-fire-whoosh_1-317280.mp3")
        self.sword_attack4_sound = pygame.mixer.Sound("assets/sfx/sword_sfx/fire-breath-6922.mp3")
        self.orc_attack_sound = pygame.mixer.Sound(
            "assets/sfx/sword_sfx/character-falling-on-ground-250069.mp3")
        self.walk_sound.set_volume(0.2)
        self.sword_attack1_sound.set_volume(0.4)
        self.sword_attack2_sound.set_volume(0.2)
        self.sword_attack3_sound.set_volume(0.15)
        self.walk_sound_playing = False
        self.attack_sound_played = False

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from sprite sheet
        animation_list = []  # A list that contains lists of rows from a sprite sheet
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(
                    pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
            # print(animation_list)

        return animation_list

    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER):
        SPEED = 6
        GRAVITY = 2
        dx = 0
        dy = 0
        FLOOR_HEIGHT = 100
        self.running = False
        self.flip = False

        # Key presses
        key = pygame.key.get_pressed()
        #
        # EDIT FOR EACH PLAYER
        # SPLIT IN TWO CLASS INSTANCES
        #
        # MOVEMENT BINDS WASD
        if PLAYER == 0:
            if key[pygame.K_d]:  # RIGHT
                dx += SPEED
                self.running = True
            if key[pygame.K_a]:  # LEFT
                dx -= SPEED
                self.running = True

        # jumping
        if PLAYER == 0:
            if key[pygame.K_w]:  # UP
                self.vel_y -= SPEED
        if PLAYER == 1:
            if key[pygame.K_SPACE]:  # UP
                self.vel_y -= SPEED

        if key[pygame.K_i]:  # FLIP TEST
            if self.flip == True:
                self.flip = False
        # MOVEMENT BINDS ARROWS
        if PLAYER == 1:
            if key[pygame.K_RIGHT]:  # RIGHT
                dx += SPEED
                self.running = True
            if key[pygame.K_LEFT]:  # LEFT
                dx -= SPEED
                self.running = True
            # jumping
            if key[pygame.K_UP]:  # UP
                self.vel_y -= SPEED

        # Attack binds
        if PLAYER == 0:
            if not self.attacking:
                if key[pygame.K_r]:
                    self.attacking = True
                    self.attack_type = 1
                    self.attack_sound_played = False
                elif key[pygame.K_f]:
                    self.attacking = True
                    self.attack_type = 2
                    self.attack_sound_played = False
                elif key[pygame.K_v]:
                    self.attacking = True
                    self.attack_type = 3
                    self.attack_sound_played = False

        # Attack binds
        if PLAYER == 1:
            if not self.attacking:
                if key[pygame.K_RCTRL]:
                    self.attacking = True
                    self.attack_type = 1
                    self.attack_sound_played = False
                elif key[pygame.K_PERIOD]:
                    self.attacking = True
                    self.attack_type = 2
                    self.attack_sound_played = False
                elif key[pygame.K_SLASH]:
                    self.attacking = True
                    self.attack_type = 3
                    self.attack_sound_played = False

        if PLAYER == 1:
            self.flip = True

        # SFX
        # walking sound
        if self.running:
            if not self.walk_sound_playing:
                self.walk_sound.play(-2)  # loop
                self.walk_sound_playing = True
        else:
            if self.walk_sound_playing:
                self.walk_sound.stop()
                self.walk_sound_playing = False
        # sword sound
        if self.attacking and not self.attack_sound_played:
            if self.attack_type == 1:
                self.sword_attack1_sound.play()
            elif self.attack_type == 2:
                self.sword_attack2_sound.play()
            elif self.attack_type == 3:
                self.sword_attack3_sound.play()
            elif self.attack_type == 4:
                self.orc_attack_sound.play()
            self.attack_sound_played = True

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

    # animation loop
    def update(self):
        animation_cooldown = 110  # change image frame every 110ms
        if self.attacking:
            if self.attack_type == 1:
                self.update_action(2)  # attack type 1
            elif self.attack_type == 2:
                self.update_action(3)  # attack type 2
            elif self.attack_type == 3:
                self.update_action(4)  # attack type 3

        elif self.running == True:
            self.update_action(1)  # walk
        else:
            self.update_action(0)  # idle

        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            if self.attacking:
                self.attacking = False
                self.attack_sound_played = False

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        # pygame.draw.rect(surface, (222, 110, 0), self.rect)
        surface.blit(img,
                     (self.rect.x - self.offset[0] * self.image_scale, self.rect.y - self.offset[1] * self.image_scale))

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the current animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
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
