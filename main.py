import pygame

import game_config as config
from enums import Colors, Sids
from starship_obj import Starship

WIN = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)


def draw_window(red, yellow):
    WIN.blit(config.SPACE_BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, Colors.BLACK.value, config.BORDER)
    red_health_text = config.HEALTH_FONT.render("Health: " + str(red.health), 1, Colors.WHITE.value)
    yellow_health_text = config.HEALTH_FONT.render("Health: " + str(yellow.health), 1, Colors.WHITE.value)
    WIN.blit(red_health_text, (config.WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(yellow.display, (yellow.location.x, yellow.location.y))
    WIN.blit(red.display, (red.location.x, red.location.y))
    for bullet in yellow.bullets.bullets_display:
        pygame.draw.rect(WIN, Colors.YELLOW.value, bullet)
    for bullet in red.bullets.bullets_display:
        pygame.draw.rect(WIN, Colors.RED.value, bullet)
    pygame.display.update()


def draw_winner(text):
    draw_text = config.WINNER_FONT.render(text, 1, Colors.WHITE.value)
    WIN.blit(draw_text,
             (config.WIDTH // 2 - draw_text.get_width() // 2, config.HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)


def main():
    red = Starship(700, 300, rotation=270, image_path=config.RED_SPACESHIP_PATH, hit_event_num=pygame.USEREVENT + 1,
                   display_side=Sids.right)
    yellow = Starship(100, 300, rotation=90, image_path=config.YELLOW_SPACESHIP_PATH,
                      hit_event_num=pygame.USEREVENT + 2, display_side=Sids.left)
    clock = pygame.time.Clock()
    winner_text = ''
    run = True
    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == red.movement_keys_system['fire']:
                red.fire_handler()
            if event.type == pygame.KEYDOWN and event.key == yellow.movement_keys_system['fire']:
                yellow.fire_handler()
            if event.type == red.hit_event_id:
                red.health -= 1
            if event.type == yellow.hit_event_id:
                yellow.health -= 1

            if red.health <= 0:
                winner_text = 'Yellow wins!'
            elif yellow.health <= 0:
                winner_text = 'Red wins!'
            if winner_text != '':
                draw_winner(winner_text)
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow.movement_handler(keys_pressed)
        red.movement_handler(keys_pressed)
        red.bullets.movement_handler(enemy_starship=yellow)
        yellow.bullets.movement_handler(enemy_starship=red)
        draw_window(red, yellow)

    pygame.event.clear()
    main()


if __name__ == '__main__':
    main()
