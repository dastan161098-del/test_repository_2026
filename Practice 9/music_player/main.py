import pygame
import sys
import os
from player import MusicPlayer

pygame.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)


base_dir = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(base_dir, "music")

player = MusicPlayer(music_path)

clock = pygame.time.Clock()


def draw_ui():
    screen.fill((20, 20, 20))


    artist, track = player.get_track_info()

    # 🎵 Track
    track_text = font.render(
        f"Track: {track}",
        True,
        (255, 255, 255)
    )
    screen.blit(track_text, (20, 40))

   
    artist_text = font.render(
        f"Artist: {artist}",
        True,
        (200, 200, 200)
    )
    screen.blit(artist_text, (20, 80))

   
    position_text = font.render(
        f"Playlist: {player.get_position()}",
        True,
        (150, 150, 255)
    )
    screen.blit(position_text, (20, 120))

    
    if player.paused:
        status = "Paused"
    elif player.is_playing:
        status = "Playing"
    else:
        status = "Stopped"

    status_text = font.render(
        f"Status: {status}",
        True,
        (0, 200, 0)
    )
    screen.blit(status_text, (20, 160))

   
    controls = [
        "P = Play / Pause",
        "S = Stop",
        "N = Next",
        "B = Previous",
        "Q = Quit"
    ]

    for i, c in enumerate(controls):
        text = font.render(c, True, (180, 180, 180))
        screen.blit(text, (20, 220 + i * 30))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                if player.is_playing:
                    player.pause()
                else:
                    player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.previous()

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    draw_ui()

    pygame.display.flip()
    clock.tick(30)