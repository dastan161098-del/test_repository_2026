import pygame

font = None
small = None


def init_fonts():
    global font, small
    font = pygame.font.SysFont("Arial", 26)
    small = pygame.font.SysFont("Arial", 20)


# BUTTON (тек draw үшін)
def draw_btn(surf, text, rect):
    pygame.draw.rect(surf, (55, 55, 75), rect)
    pygame.draw.rect(surf, (200, 200, 200), rect, 2)

    t = font.render(text, True, (255, 255, 255))
    surf.blit(
        t,
        (rect.centerx - t.get_width() // 2,
         rect.centery - t.get_height() // 2)
    )


# HITBOX CHECK
def is_clicked(rect, mx, my, event):
    return event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(mx, my)


def main_menu(surf, clock):
    init_fonts()
    big = pygame.font.SysFont("Arial", 52, bold=True)

    while True:
        surf.fill((20, 20, 40))

        mx, my = pygame.mouse.get_pos()

        play_btn = pygame.Rect(150, 210, 200, 44)
        lb_btn = pygame.Rect(150, 265, 200, 44)
        settings_btn = pygame.Rect(150, 320, 200, 44)
        quit_btn = pygame.Rect(150, 375, 200, 44)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"

            if is_clicked(play_btn, mx, my, e):
                return "play"
            if is_clicked(lb_btn, mx, my, e):
                return "lb"
            if is_clicked(settings_btn, mx, my, e):
                return "settings"
            if is_clicked(quit_btn, mx, my, e):
                return "quit"

        t = big.render("RACER", True, (230, 190, 0))
        surf.blit(t, (250 - t.get_width() // 2, 120))

        draw_btn(surf, "Play", play_btn)
        draw_btn(surf, "Leaderboard", lb_btn)
        draw_btn(surf, "Settings", settings_btn)
        draw_btn(surf, "Quit", quit_btn)

        pygame.display.flip()
        clock.tick(60)


def ask_name(surf, clock):
    init_fonts()
    name = ""

    while True:
        surf.fill((20, 20, 40))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return ""

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and name:
                    return name
                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 14 and e.unicode.isprintable():
                    name += e.unicode

        surf.blit(font.render("Enter your name:", True, (255, 255, 255)), (145, 220))

        box = pygame.Rect(120, 265, 260, 40)
        pygame.draw.rect(surf, (50, 50, 70), box)
        pygame.draw.rect(surf, (255, 255, 255), box, 2)

        surf.blit(font.render(name + "|", True, (230, 190, 0)), (130, 272))
        surf.blit(small.render("Press Enter to start", True, (150, 150, 150)), (160, 320))

        pygame.display.flip()
        clock.tick(60)


def settings_screen(surf, clock, settings):
    init_fonts()

    colors = ["red", "blue", "green"]
    diffs = ["easy", "normal", "hard"]

    while True:
        surf.fill((20, 20, 40))
        mx, my = pygame.mouse.get_pos()

        color_btn = pygame.Rect(240, 220, 130, 38)
        diff_btn = pygame.Rect(240, 275, 130, 38)
        sound_btn = pygame.Rect(240, 330, 130, 38)
        back_btn = pygame.Rect(155, 430, 200, 44)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return settings

            if is_clicked(back_btn, mx, my, e):
                return settings

            if is_clicked(color_btn, mx, my, e):
                i = colors.index(settings["color"])
                settings["color"] = colors[(i + 1) % len(colors)]

            if is_clicked(diff_btn, mx, my, e):
                i = diffs.index(settings["difficulty"])
                settings["difficulty"] = diffs[(i + 1) % len(diffs)]

            if is_clicked(sound_btn, mx, my, e):
                settings["music"] = not settings.get("music", True)

        surf.blit(font.render("Settings", True, (255, 255, 255)), (195, 155))

        surf.blit(font.render("Car color:", True, (180, 180, 180)), (70, 227))
        surf.blit(font.render("Difficulty:", True, (180, 180, 180)), (70, 282))
        surf.blit(font.render("Music:", True, (180, 180, 180)), (70, 337))

        draw_btn(surf, settings["color"], color_btn)
        draw_btn(surf, settings["difficulty"], diff_btn)
        draw_btn(surf, "ON" if settings["music"] else "OFF", sound_btn)
        draw_btn(surf, "Back", back_btn)

        pygame.display.flip()
        clock.tick(60)


def leaderboard_screen(surf, clock):
    from persistence import load_scores
    init_fonts()

    data = load_scores()

    while True:
        surf.fill((20, 20, 40))

        mx, my = pygame.mouse.get_pos()
        back_btn = pygame.Rect(155, 530, 200, 44)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

            if is_clicked(back_btn, mx, my, e):
                return

        surf.blit(font.render("Top 10", True, (230, 190, 0)), (205, 45))
        surf.blit(small.render("# Name Score Dist Coins", True, (150, 150, 150)), (45, 90))

        for i, d in enumerate(data):
            col = (230, 190, 0) if i == 0 else (255, 255, 255)
            row = f"{i+1:<3} {d['name']:<10} {d['score']:<6} {d['dist']:<6} {d['coins']}"
            surf.blit(small.render(row, True, col), (45, 120 + i * 30))

        draw_btn(surf, "Back", back_btn)

        pygame.display.flip()
        clock.tick(60)


def gameover_screen(surf, clock, score, dist, coins):
    init_fonts()
    big = pygame.font.SysFont("Arial", 48, bold=True)

    while True:
        surf.fill((20, 20, 40))
        mx, my = pygame.mouse.get_pos()

        retry_btn = pygame.Rect(150, 385, 200, 44)
        menu_btn = pygame.Rect(150, 445, 200, 44)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"

            if is_clicked(retry_btn, mx, my, e):
                return "retry"

            if is_clicked(menu_btn, mx, my, e):
                return "menu"

        t = big.render("GAME OVER", True, (220, 50, 50))
        surf.blit(t, (250 - t.get_width() // 2, 115))

        surf.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (170, 235))
        surf.blit(font.render(f"Distance: {dist}m", True, (255, 255, 255)), (150, 278))
        surf.blit(font.render(f"Coins: {coins}", True, (255, 255, 255)), (170, 321))

        draw_btn(surf, "Retry", retry_btn)
        draw_btn(surf, "Main Menu", menu_btn)

        pygame.display.flip()
        clock.tick(60)