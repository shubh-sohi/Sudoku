import random

from Sudoku.Sudoku_fill import filler
from Sudoku.Sudoku_helper import get_numbers, is_cursor_inside
from Sudoku.Sudoku_hover import hover_main, clicked_hover
from Sudoku.Sudoku_texts import *

from Sudoku.GUI.Sudoku_numbers import *

pygame.init()
heading = pygame.display.set_caption("Sudoku")


def draw_grid():
    for j in range(9):
        for i in range(9):
            pygame.draw.rect(screen, ((102, 178, 255)), (((i * 50) + 450), ((j * 50) + 50), 50, 50), 2)
        pygame.draw.rect(screen, ((102, 178, 255)), (((j * 50) + 450), 550, 50, 50), 2)

    for a in range(3):
        pygame.draw.rect(screen, ((0, 0, 160)), (((a * 150) + 450), 50, 150, 150), 5)
        pygame.draw.rect(screen, ((0, 0, 160)), (((a * 150) + 450), 200, 150, 150), 5)
        pygame.draw.rect(screen, ((0, 0, 160)), (((a * 150) + 450), 350, 150, 150), 5)
        pygame.draw.rect(screen, ((0, 0, 160)), (450, 550, 450, 50), 5)


# def screen_effect(count):
#     if count == 50:
#         count = 0
#     screen.fill((204 + count, 229, 255))
def change_color():
    global is_top_hit, is_bottom_hit, a, crazy_color_counter
    if a == 150:
        is_top_hit = True
        is_bottom_hit = False
    if a == 5:
        is_top_hit = False
        is_bottom_hit = True
    if is_bottom_hit:
        a += 1
    if is_top_hit:
        a -= 1
    if crazy_color_counter % 2 == 0:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    else:
        screen.fill((80 + a, 100 + a, 80 + a))


a = 0
crazy_color_counter = 1
is_top_hit = False
is_bottom_hit = True
finalize = False
is_clicked = False
key = None
pen_down_mouse = pygame.mouse.get_pos()


def main():
    global is_clicked, key, finalize, pen_down_mouse, \
        crazy_color_counter

    running = True
    while running:

        change_color()
        draw_grid()
        text_main()
        initial_fillup()
        if not is_clicked:
            pen_down_mouse = pygame.mouse.get_pos()
            hover_main()
            get_numbers(pen_down_mouse, is_clicked)

        else:
            clicked_hover(pen_down_mouse)
            get_numbers(pen_down_mouse, is_clicked)
            filler(key, pen_down_mouse, finalize)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cracy_color_mouse = pygame.mouse.get_pos()
                if 35 < cracy_color_mouse[0] < 405 and 40 < cracy_color_mouse[1] < 120:
                    crazy_color_counter += 1
                if is_cursor_inside():
                    key = None
                    pen_down_mouse = pygame.mouse.get_pos()
                    is_clicked = True
                    finalize = False
                else:
                    is_clicked = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                    finalize = False
                if event.key == pygame.K_2:
                    key = 2
                    finalize = False
                if event.key == pygame.K_3:
                    key = 3
                    finalize = False
                if event.key == pygame.K_4:
                    key = 4
                    finalize = False
                if event.key == pygame.K_5:
                    key = 5
                    finalize = False
                if event.key == pygame.K_6:
                    key = 6
                    finalize = False
                if event.key == pygame.K_7:
                    key = 7
                    finalize = False
                if event.key == pygame.K_8:
                    key = 8
                    finalize = False
                if event.key == pygame.K_9:
                    key = 9
                    finalize = False
                if event.key == pygame.K_RETURN:
                    finalize = True


if __name__ == "__main__":
    main()
