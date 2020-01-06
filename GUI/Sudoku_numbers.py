from Sudoku.GUI.Sudoku_texts import pygame, screen
from Sudoku.Solver.Sudoku_init import Sudoku

padding = 25


def initial_fillup():
    grid = Sudoku
    cube_dim = 50
    num_font = pygame.font.SysFont("phosphate", 40)
    grid_start_Y = 50
    for row in range(len(grid)):
        grid_start_X = 450
        for coln in range(len(grid)):
            if Sudoku[row][coln] != 0:
                num = num_font.render(str(Sudoku[row][coln]), True, ((255, 0, 127)), None)
                numHelper = num.get_rect()
                numHelper.center = (grid_start_X + padding, grid_start_Y + padding)
                screen.blit(num, numHelper)
                grid_start_X += cube_dim
            else:
                grid_start_X += cube_dim
        grid_start_Y += cube_dim
