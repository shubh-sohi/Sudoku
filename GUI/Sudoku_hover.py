from Sudoku.GUI.Sudoku_texts import screen, pygame
from Sudoku.Solver.Sudoku_init import Sudoku

# from Sudoku.Sudoku_game import is_clicked

PINK = ((255, 0, 127))
BLUE = ((102, 178, 255))
ROW_LENGTH = 50
ROW_HEIGHT = 450
COLN_LENGTH = 450
COLN_HEIGHT = 50
SUBGRID_LENGTH = 150
SUBGRID_HEIGHT = 150
GRID_X = (450, 900)
GRID_Y = (50, 500)


def is_cursor_inside():
    mouse = pygame.mouse.get_pos()
    if GRID_X[0] < mouse[0] < GRID_X[1] and GRID_Y[0] < mouse[1] < GRID_Y[1]:
        return True
    else:
        return False


def hover_row():
    mouse = pygame.mouse.get_pos()
    if is_cursor_inside():
        num_row = mouse[1] // 50
        pygame.draw.rect(screen, PINK, (GRID_X[0], num_row * 50, COLN_LENGTH, COLN_HEIGHT), 5)
        # print(num_coln)


def hover_coln():
    mouse = pygame.mouse.get_pos()
    if is_cursor_inside():
        num_coln = mouse[0] // 50 - 9
        pygame.draw.rect(screen, PINK, ((num_coln * 50) + 450, GRID_Y[0], ROW_LENGTH, ROW_HEIGHT), 5)
        # print(num_coln)


def hover_subgrid():
    mouse = pygame.mouse.get_pos()
    if is_cursor_inside():
        num_row = mouse[1] // 50
        num_coln = mouse[0] // 50 - 8
        if num_row <= 3:
            if num_coln <= 3:
                pygame.draw.rect(screen, PINK, (450, 50, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 3 < num_coln <= 6:
                pygame.draw.rect(screen, PINK, (600, 50, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 6 < num_coln <= 9:
                pygame.draw.rect(screen, PINK, (750, 50, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
        if 3 < num_row <= 6:
            if num_coln <= 3:
                pygame.draw.rect(screen, PINK, (450, 200, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 3 < num_coln <= 6:
                pygame.draw.rect(screen, PINK, (600, 200, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 6 < num_coln <= 9:
                pygame.draw.rect(screen, PINK, (750, 200, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
        if 6 < num_row <= 9:
            if num_coln <= 3:
                pygame.draw.rect(screen, PINK, (450, 350, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 3 < num_coln <= 6:
                pygame.draw.rect(screen, PINK, (600, 350, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)
            if 6 < num_coln <= 9:
                pygame.draw.rect(screen, PINK, (750, 350, SUBGRID_LENGTH, SUBGRID_HEIGHT), 5)


def clicked_hover(mouse_coordinates):
    num_row = mouse_coordinates[1] // 50
    num_coln = mouse_coordinates[0] // 50 - 9
    if Sudoku[num_row - 1][num_coln] == 0:
        pygame.draw.rect(screen, PINK, (GRID_X[0], (num_row * 50), COLN_LENGTH, COLN_HEIGHT), 5)
        pygame.draw.rect(screen, PINK, ((num_coln * 50) + 450, GRID_Y[0], ROW_LENGTH, ROW_HEIGHT), 5)
        pygame.draw.rect(screen, BLUE, ((num_coln * 50) + 450, (num_row * 50), 50, 50), 5)
    else:
        hover_main()


def hover_main():
    hover_coln()
    hover_row()
    hover_subgrid()
