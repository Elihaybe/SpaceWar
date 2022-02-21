import pygame
from enums import Sids
from starship_obj import Starship
import game_config as config


class Bullets:
    width = 20
    height = 10
    vel = 7
    max_bullets = 5

    def __init__(self, starship_side):
        self.Bullets_display = []
        self.starship_side = starship_side

    def count(self):
        return len(self.Bullets_display)

    def append_bullet(self, x, y):
        if self.starship_side == Sids.left:
            x += self.width
        y += (Starship.height // 2) + 5
        blt = pygame.Rect(x, y, self.width, self.height)
        self.Bullets_display.append(blt)

    def remove_bullet(self, blt):
        self.Bullets_display.remove(blt)

    def handler(self, enemy_starship):
        for blt in self.Bullets_display:
            blt.x += Bullets.vel
            if enemy_starship.colliderect(blt):
                self.remove_bullet(blt)
                pygame.event.post(pygame.event.Event(enemy_starship.hit_event_id))
            elif (self.starship_side == Sids.left and blt.x > config.WIDTH) or (
                    self.starship_side == Sids.right and blt.x < 0):
                self.remove_bullet(blt)
