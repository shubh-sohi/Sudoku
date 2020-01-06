from Sudoku.Sudoku_hover import is_cursor_inside

from Sudoku.GUI.Sudoku_numbers import pygame, screen
from Sudoku.Solver.Sudoku_init import get_values, Sudoku


def get_numbers(helper_mouse, is_clicked):
    num_font = pygame.font.SysFont("phosphate", 40)
    if is_cursor_inside() or is_clicked:
        num_row = helper_mouse[1] // 50 - 1
        num_coln = helper_mouse[0] // 50 - 9
        if Sudoku[num_row][num_coln] == 0:
            buffer = get_values(num_row, num_coln, Sudoku)
            for i in range(1, 10):
                if i not in buffer:
                    num = num_font.render(str(i), True, ((255, 0, 127)), None)
                    numHelper = num.get_rect()
                    numHelper.center = (425 + (i * 50), 575)
                    screen.blit(num, numHelper)
