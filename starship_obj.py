import pygame
import game_config as config
from bullet_obj import Bullets
from enums import Sids


class Starship:
    lives = 10
    width = 100
    height = 85
    vel = 5
    wdsa_keys = {"up": pygame.K_w,
                 "down": pygame.K_s,
                 "right": pygame.K_d,
                 "left": pygame.K_a,
                 "fire": pygame.K_TAB}
    arrow_keys = {"up": pygame.K_UP,
                  "down": pygame.K_DOWN,
                  "right": pygame.K_RIGHT,
                  "left": pygame.K_LEFT,
                  "fire": pygame.K_SPACE}

    def __init__(self, x, y, rotation, image_path, hit_event_num, display_side):
        self.location = pygame.Rect(x, y, self.width, self.height)
        self.display_side = display_side
        self.bullets = Bullets(self.display_side)
        self.health = self.lives
        self.image = pygame.image.load(image_path)
        self.display = pygame.transform.rotate(pygame.transform.scale(self.image, (self.width, self.height)), rotation)
        self.hit_event_id = hit_event_num
        self.movement_keys_system = self.arrow_keys if display_side == Sids.right else self.wdsa_keys

    def update_location(self, x=None, y=None):
        if x is not None:
            self.location.x = x
        if y is not None:
            self.location.y = y

    def movement_handler(self, keys_pressed):
        if self.display_side == Sids.right:
            left_border = config.BORDER.x + config.BORDER.width
            right_border = config.WIDTH
        else:
            left_border = 0
            right_border = config.BORDER.x
        if keys_pressed[self.movement_keys_system['left']] and self.location.x - self.vel > left_border:
            self.update_location(x=self.location.x - self.vel)
        if keys_pressed[
            self.movement_keys_system['right']] and self.location.x + self.vel + self.location.width < right_border:
            self.update_location(x=self.location.x + self.vel)
        if keys_pressed[self.movement_keys_system['up']] and self.location.y - self.vel > 0:
            self.location.y -= self.vel
        if keys_pressed[self.movement_keys_system[
            'down']] and self.location.y + self.vel + self.location.height < config.HEIGHT - 15:
            self.location.y += self.vel

    def fire_handler(self, fire_sound=None):
        if self.bullets.count() < Bullets.max_bullets:
            self.bullets.append_bullet(self.location.x, self.location.y)
            if fire_sound:
                pygame.mixer.init()
                pygame.mixer.music.load(fire_sound)
                pygame.mixer.music.play()
