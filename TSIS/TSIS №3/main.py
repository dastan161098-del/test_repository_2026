import pygame
import sys

from persistence import load_settings, save_settings, save_score
from ui import main_menu, ask_name, settings_screen, leaderboard_screen, gameover_screen
from racer import run

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

settings = load_settings()

# MUSIC
pygame.mixer.music.load("TSIS №3/background.wav")
pygame.mixer.music.set_volume(0.5)


def update_sound():
   
    if settings.get("music", True):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()


coin_sound = pygame.mixer.Sound("TSIS №3/coin.wav")
crash_sound = pygame.mixer.Sound("TSIS №3/crash.wav")


def draw_road():
    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 255), (150, 0, 5, 600))
    pygame.draw.rect(screen, (255, 255, 255), (250, 0, 5, 600))
    pygame.draw.rect(screen, (255, 255, 255), (350, 0, 5, 600))


while True:

    update_sound()

    action = main_menu(screen, clock)

    if action == "quit":
        save_settings(settings)
        pygame.quit()
        sys.exit()

    elif action == "lb":
        leaderboard_screen(screen, clock)

    elif action == "settings":
        settings = settings_screen(screen, clock, settings)
        save_settings(settings)
        update_sound()

    elif action == "play":
        name = ask_name(screen, clock)
        if not name:
            continue

        while True:
            draw_road()

            score, dist, coins = run(screen, clock, settings, name)

            save_score(name, score, dist, coins)

            result = gameover_screen(screen, clock, score, dist, coins)

            if result == "menu":
                break

            elif result == "quit":
                save_settings(settings)
                pygame.quit()
                sys.exit()