import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
TOOLBAR_HEIGHT = 80

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)

MODE_BRUSH = "brush"
MODE_RECT = "rectangle"
MODE_CIRCLE = "circle"
MODE_ERASER = "eraser"
MODE_SQUARE = "square"
MODE_RIGHT_TRIANGLE = "right_triangle"
MODE_EQ_TRIANGLE = "equilateral_triangle"
MODE_RHOMBUS = "rhombus"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint Program")
clock = pygame.time.Clock()


class Button:
    def __init__(self, x, y, width, height, color, text="", text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class ColorPalette:
    def __init__(self, x, y):
        self.colors = [
            BLACK, WHITE, RED, GREEN, BLUE,
            YELLOW, CYAN, MAGENTA, ORANGE,
            PURPLE, GRAY
        ]
        self.color_rects = []
        self.selected_color = BLACK

        for i, color in enumerate(self.colors):
            rect = pygame.Rect(x + i * 35, y, 30, 30)
            self.color_rects.append((rect, color))

    def draw(self, surface):
        for rect, color in self.color_rects:
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

            if color == self.selected_color:
                pygame.draw.rect(surface, WHITE, rect, 3)

    def check_click(self, pos):
        for rect, color in self.color_rects:
            if rect.collidepoint(pos):
                self.selected_color = color
                return True
        return False


def main():
    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - TOOLBAR_HEIGHT))
    canvas.fill(WHITE)

    drawing = False
    start_pos = None
    current_mode = MODE_BRUSH
    brush_size = 5
    eraser_size = 20
    current_color = BLACK

    buttons = [
        Button(10, 10, 70, 30, GRAY, "Brush"),
        Button(90, 10, 70, 30, GRAY, "Rect"),
        Button(170, 10, 70, 30, GRAY, "Circle"),
        Button(250, 10, 70, 30, GRAY, "Eraser"),
        Button(330, 10, 70, 30, GRAY, "Square"),
        Button(410, 10, 70, 30, GRAY, "R-Tri"),
        Button(490, 10, 70, 30, GRAY, "E-Tri"),
        Button(570, 10, 70, 30, GRAY, "Rhomb"),
        Button(650, 10, 70, 30, WHITE, "Clear")
    ]

    color_palette = ColorPalette(10, 50)

    size_up_btn = Button(800, 10, 40, 30, GRAY, "+")
    size_down_btn = Button(850, 10, 40, 30, GRAY, "-")

    font = pygame.font.Font(None, 24)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if y < TOOLBAR_HEIGHT:
                    if buttons[0].is_clicked(event.pos):
                        current_mode = MODE_BRUSH
                    elif buttons[1].is_clicked(event.pos):
                        current_mode = MODE_RECT
                    elif buttons[2].is_clicked(event.pos):
                        current_mode = MODE_CIRCLE
                    elif buttons[3].is_clicked(event.pos):
                        current_mode = MODE_ERASER
                    elif buttons[4].is_clicked(event.pos):
                        current_mode = MODE_SQUARE
                    elif buttons[5].is_clicked(event.pos):
                        current_mode = MODE_RIGHT_TRIANGLE
                    elif buttons[6].is_clicked(event.pos):
                        current_mode = MODE_EQ_TRIANGLE
                    elif buttons[7].is_clicked(event.pos):
                        current_mode = MODE_RHOMBUS
                    elif buttons[8].is_clicked(event.pos):
                        canvas.fill(WHITE)

                    if size_up_btn.is_clicked(event.pos):
                        brush_size = min(50, brush_size + 2)
                        eraser_size = min(50, eraser_size + 2)

                    elif size_down_btn.is_clicked(event.pos):
                        brush_size = max(1, brush_size - 2)
                        eraser_size = max(5, eraser_size - 2)

                    color_palette.check_click(event.pos)
                    current_color = color_palette.selected_color

                else:
                    drawing = True
                    start_pos = (x, y - TOOLBAR_HEIGHT)

                    if current_mode == MODE_BRUSH:
                        pygame.draw.circle(canvas, current_color, start_pos, brush_size)

                    elif current_mode == MODE_ERASER:
                        pygame.draw.circle(canvas, WHITE, start_pos, eraser_size)

            elif event.type == pygame.MOUSEMOTION:
                if drawing and current_mode in [MODE_BRUSH, MODE_ERASER]:
                    x, y = event.pos

                    if y > TOOLBAR_HEIGHT:
                        current_pos = (x, y - TOOLBAR_HEIGHT)

                        if start_pos:
                            dx = current_pos[0] - start_pos[0]
                            dy = current_pos[1] - start_pos[1]
                            distance = max(abs(dx), abs(dy))

                            if distance == 0:
                                distance = 1

                            for i in range(distance):
                                px = int(start_pos[0] + dx * i / distance)
                                py = int(start_pos[1] + dy * i / distance)

                                if current_mode == MODE_BRUSH:
                                    pygame.draw.circle(
                                        canvas,
                                        current_color,
                                        (px, py),
                                        brush_size
                                    )
                                else:
                                    pygame.draw.circle(
                                        canvas,
                                        WHITE,
                                        (px, py),
                                        eraser_size
                                    )

                        start_pos = current_pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    x, y = event.pos

                    if y > TOOLBAR_HEIGHT:
                        end_pos = (x, y - TOOLBAR_HEIGHT)

                        if current_mode == MODE_RECT:
                            rect = pygame.Rect(
                                start_pos[0],
                                start_pos[1],
                                end_pos[0] - start_pos[0],
                                end_pos[1] - start_pos[1]
                            )
                            pygame.draw.rect(canvas, current_color, rect, 2)

                        elif current_mode == MODE_CIRCLE:
                            radius = int(
                                ((end_pos[0] - start_pos[0]) ** 2 +
                                 (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                            )
                            pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                        elif current_mode == MODE_SQUARE:
                            side = max(
                                abs(end_pos[0] - start_pos[0]),
                                abs(end_pos[1] - start_pos[1])
                            )

                            x1 = start_pos[0]
                            y1 = start_pos[1]

                            if end_pos[0] < x1:
                                x1 -= side
                            if end_pos[1] < y1:
                                y1 -= side

                            pygame.draw.rect(
                                canvas,
                                current_color,
                                (x1, y1, side, side),
                                2
                            )

                        elif current_mode == MODE_RIGHT_TRIANGLE:
                            points = [
                                start_pos,
                                (start_pos[0], end_pos[1]),
                                end_pos
                            ]
                            pygame.draw.polygon(canvas, current_color, points, 2)

                        elif current_mode == MODE_EQ_TRIANGLE:
                            side = abs(end_pos[0] - start_pos[0])

                            if side < 1:
                                side = 1

                            height = int((math.sqrt(3) / 2) * side)

                            points = [
                                (start_pos[0], start_pos[1] + height),
                                (start_pos[0] + side, start_pos[1] + height),
                                (start_pos[0] + side // 2, start_pos[1])
                            ]

                            pygame.draw.polygon(canvas, current_color, points, 2)

                        elif current_mode == MODE_RHOMBUS:
                            center_x = (start_pos[0] + end_pos[0]) // 2
                            center_y = (start_pos[1] + end_pos[1]) // 2

                            width = abs(end_pos[0] - start_pos[0])
                            height = abs(end_pos[1] - start_pos[1])

                            points = [
                                (center_x, center_y - height // 2),
                                (center_x + width // 2, center_y),
                                (center_x, center_y + height // 2),
                                (center_x - width // 2, center_y)
                            ]

                            pygame.draw.polygon(canvas, current_color, points, 2)

                drawing = False
                start_pos = None

        screen.fill(GRAY)
        screen.blit(canvas, (0, TOOLBAR_HEIGHT))

        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (0, 0, SCREEN_WIDTH, TOOLBAR_HEIGHT)
        )

        pygame.draw.line(
            screen,
            BLACK,
            (0, TOOLBAR_HEIGHT),
            (SCREEN_WIDTH, TOOLBAR_HEIGHT),
            2
        )

        for button in buttons:
            button.draw(screen)

        color_palette.draw(screen)

        size_up_btn.draw(screen)
        size_down_btn.draw(screen)

        size_text = font.render(f"Size: {brush_size}", True, BLACK)
        screen.blit(size_text, (800, 50))

        mode_text = font.render(f"Mode: {current_mode}", True, BLACK)
        screen.blit(mode_text, (650, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()