import pygame
import sys
from pygame.locals import *
import random
import time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

COINS_FOR_SPEED_UP = 5

COIN_TYPES = {
    "bronze": 1,
    "silver": 2,
    "gold": 3
}

font_big = pygame.font.SysFont("Verdana", 50)
font_medium = pygame.font.SysFont("Verdana", 28)
font_small = pygame.font.SysFont("Verdana", 20)


def load_image(filename, default_color, width, height):
    try:
        path = os.path.join("images", filename)

        if os.path.exists(path):
            image = pygame.image.load(path)
        else:
            image = pygame.image.load(filename)

        image = pygame.transform.scale(image, (width, height))
        return image

    except:
        image = pygame.Surface((width, height))
        image.fill(default_color)
        return image


background = load_image(
    "racer/AnimatedStreet.png",
    GRAY,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

player_img = load_image(
    "racer/Player.png",
    BLUE,
    50,
    80
)

enemy_img = load_image(
    "racer/Enemy.png",
    RED,
    50,
    80
)

coin_img = load_image(
    "racer/coin.png",
    YELLOW,
    30,
    30
)

DISPLAYSURF = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Street Racer")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = player_img
        self.rect = self.image.get_rect()

        self.rect.center = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 80
        )

        self.speed = 7

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

        if (pressed_keys[K_RIGHT] or pressed_keys[K_d]) and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = enemy_img
        self.rect = self.image.get_rect()

        self.reset_position()

    def reset_position(self):
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            0
        )

    def move(self):
        global SCORE

        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = coin_img
        self.rect = self.image.get_rect()

        self.set_coin_type()
        self.reset_position()

    def set_coin_type(self):
        self.coin_type = random.choice(
            list(COIN_TYPES.keys())
        )

        self.value = COIN_TYPES[self.coin_type]

    def reset_position(self):
        self.set_coin_type()

        self.rect.center = (
            random.randint(30, SCREEN_WIDTH - 30),
            random.randint(-400, -100)
        )

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def show_game_over():
    DISPLAYSURF.fill(RED)

    game_over_text = font_big.render(
        "GAME OVER",
        True,
        BLACK
    )

    score_text = font_medium.render(
        f"Score: {SCORE}",
        True,
        WHITE
    )

    coin_text = font_medium.render(
        f"Coins: {COINS_COLLECTED}",
        True,
        YELLOW
    )

    restart_text = font_small.render(
        "SPACE - Restart",
        True,
        GREEN
    )

    quit_text = font_small.render(
        "ESC - Quit",
        True,
        GREEN
    )

    DISPLAYSURF.blit(
        game_over_text,
        (
            SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
            150
        )
    )

    DISPLAYSURF.blit(
        score_text,
        (
            SCREEN_WIDTH // 2 - score_text.get_width() // 2,
            250
        )
    )

    DISPLAYSURF.blit(
        coin_text,
        (
            SCREEN_WIDTH // 2 - coin_text.get_width() // 2,
            300
        )
    )

    DISPLAYSURF.blit(
        restart_text,
        (
            SCREEN_WIDTH // 2 - restart_text.get_width() // 2,
            400
        )
    )

    DISPLAYSURF.blit(
        quit_text,
        (
            SCREEN_WIDTH // 2 - quit_text.get_width() // 2,
            440
        )
    )

    pygame.display.update()


def reset_game():
    global SCORE, COINS_COLLECTED, SPEED

    SCORE = 0
    COINS_COLLECTED = 0
    SPEED = 5

    P1.rect.center = (
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT - 80
    )

    E1.reset_position()

    for coin in coins:
        coin.reset_position()


P1 = Player()
E1 = Enemy()

coin1 = Coin()
coin2 = Coin()

coins = pygame.sprite.Group()
coins.add(coin1)
coins.add(coin2)

PLAYING = 0
GAME_OVER = 1

game_state = PLAYING

bg_y = 0
bg_speed = 2

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_state == GAME_OVER:
            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    reset_game()
                    game_state = PLAYING

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    if game_state == PLAYING:

        bg_y = (bg_y + bg_speed) % SCREEN_HEIGHT

        DISPLAYSURF.blit(
            background,
            (0, bg_y - SCREEN_HEIGHT)
        )

        DISPLAYSURF.blit(
            background,
            (0, bg_y)
        )

        P1.move()
        E1.move()

        for coin in coins:
            coin.move()

        for coin in coins:

            if P1.rect.colliderect(coin.rect):

                COINS_COLLECTED += coin.value
                SCORE += coin.value * 10

                if COINS_COLLECTED % COINS_FOR_SPEED_UP == 0:
                    SPEED += 1

                coin.reset_position()

        if P1.rect.colliderect(E1.rect):
            time.sleep(0.5)
            game_state = GAME_OVER

        P1.draw(DISPLAYSURF)
        E1.draw(DISPLAYSURF)

        for coin in coins:
            coin.draw(DISPLAYSURF)

        pygame.draw.rect(
            DISPLAYSURF,
            WHITE,
            (5, 5, 170, 90)
        )

        pygame.draw.rect(
            DISPLAYSURF,
            BLACK,
            (5, 5, 170, 90),
            2
        )

        score_text = font_small.render(
            f"Score: {SCORE}",
            True,
            BLACK
        )

        coins_text = font_small.render(
            f"Coins: {COINS_COLLECTED}",
            True,
            BLACK
        )

        speed_text = font_small.render(
            f"Speed: {SPEED}",
            True,
            RED
        )

        DISPLAYSURF.blit(score_text, (10, 10))
        DISPLAYSURF.blit(coins_text, (10, 35))
        DISPLAYSURF.blit(speed_text, (10, 60))

        pygame.display.update()
        FramePerSec.tick(FPS)

    else:
        show_game_over()