import pygame
from enums import Sids
import starship_obj
import game_config as config


class Bullets:
    width = 20
    height = 10
    vel = 7
    max_bullets = 15

    def __init__(self, starship_side):
        self.bullets_display = []
        self.starship_side = starship_side

    def count(self):
        return len(self.bullets_display)

    def append_bullet(self, x, y):
        if self.starship_side == Sids.left:
            x += starship_obj.Starship.width
        y += (starship_obj.Starship.height // 2) + 5
        blt = pygame.Rect(x, y, self.width, self.height)
        self.bullets_display.append(blt)

    def remove_bullet(self, blt):
        self.bullets_display.remove(blt)

    def movement_handler(self, enemy_starship):
        for blt in self.bullets_display:
            if self.starship_side == Sids.left:
                blt.x += Bullets.vel
            else:
                blt.x -= Bullets.vel
            if enemy_starship.location.colliderect(blt):
                self.remove_bullet(blt)
                pygame.event.post(pygame.event.Event(enemy_starship.hit_event_id))
            elif (self.starship_side == Sids.left and blt.x > config.WIDTH) or (
                    self.starship_side == Sids.right and blt.x < 0):
                self.remove_bullet(blt)
