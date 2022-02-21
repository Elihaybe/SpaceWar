import pygame
import game_config as config

WIN = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(config.SPACE_BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, config.BLACK, config.BORDER)
    red_health_text = config.HEALTH_FONT.render("Health: " + str(red_health), 1, config.WHITE)
    yellow_health_text = config.HEALTH_FONT.render("Health: " + str(yellow_health), 1, config.WHITE)
    WIN.blit(red_health_text, (config.WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(config.YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(config.RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, config.YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, config.RED, bullet)
    pygame.display.update()


def draw_winner(text):
    draw_text = config.WINNER_FONT.render(text, 1, config.WHITE)
    WIN.blit(draw_text,
             (config.WIDTH // 2 - draw_text.get_width() // 2, config.HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)


def yellow_movement_handler(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - config.SPACESHIP_VEL > 0:  # LEFT
        yellow.x -= config.SPACESHIP_VEL
    if keys_pressed[pygame.K_d] and yellow.x + config.SPACESHIP_VEL + yellow.width < config.BORDER.x:  # RIGHT
        yellow.x += config.SPACESHIP_VEL
    if keys_pressed[pygame.K_w] and yellow.y - config.SPACESHIP_VEL > 0:  # UP
        yellow.y -= config.SPACESHIP_VEL
    if keys_pressed[pygame.K_s] and yellow.y + config.SPACESHIP_VEL + yellow.height < config.HEIGHT - 15:  # DOWN
        yellow.y += config.SPACESHIP_VEL


def red_movement_handler(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - config.SPACESHIP_VEL > config.BORDER.x + config.BORDER.width:  # LEFT
        red.x -= config.SPACESHIP_VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + config.SPACESHIP_VEL + red.width < config.WIDTH:  # RIGHT
        red.x += config.SPACESHIP_VEL
    if keys_pressed[pygame.K_UP] and red.y - config.SPACESHIP_VEL > 0:  # UP
        red.y -= config.SPACESHIP_VEL
    if keys_pressed[pygame.K_DOWN] and red.y + config.SPACESHIP_VEL + red.height < config.HEIGHT - 15:  # DOWN
        red.y += config.SPACESHIP_VEL


def bullet_handler(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += config.BULLET_VEL
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(config.RED_HIT))
        elif bullet.x > config.WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= config.BULLET_VEL
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(config.YELLOW_HIT))
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    red = pygame.Rect(700, 300, config.SPACESHIP_WIDTH, config.SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, config.SPACESHIP_WIDTH, config.SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    yellow_health = 10
    red_health = 10
    clock = pygame.time.Clock()
    winner_text = ''
    run = True
    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and len(yellow_bullets) < config.MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + (yellow.height // 2) + 5, 20, 10)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_SPACE and len(red_bullets) < config.MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + (red.height // 2) + 5, 20, 10)
                    red_bullets.append(bullet)
            if event.type == config.RED_HIT:
                red_health -= 1
            if event.type == config.YELLOW_HIT:
                yellow_health -= 1

            if red_health <= 0:
                winner_text = 'Yellow wins!'
                red_bullets = []
                yellow_bullets = []
            elif yellow_health <= 0:
                winner_text = 'Red wins!'
                yellow_bullets = []
                red_bullets = []
            if winner_text != '':
                draw_winner(winner_text)
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_movement_handler(keys_pressed=keys_pressed, yellow=yellow)
        red_movement_handler(keys_pressed=keys_pressed, red=red)
        bullet_handler(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.event.clear()
    main()


if __name__ == '__main__':
    main()
