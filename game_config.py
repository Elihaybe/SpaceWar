import pygame
import os

pygame.font.init()
pygame.display.init()

GAME_TITLE = 'Starship War'
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
FPS = 60

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
YELLOW_SPACESHIP_PATH = os.path.join('Assets', 'spaceship_yellow.png')
RED_SPACESHIP_PATH = os.path.join('Assets', 'spaceship_red.png')
RED_FIRE_SOUND_PATH = os.path.join('Assets', 'laser_sound.mp3')
YELLOW_FIRE_SOUND_PATH = os.path.join('Assets', 'gun_sound.mp3')
