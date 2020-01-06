from Sudoku.GUI.Sudoku_texts import pygame
from Sudoku.GUI.Sudoku_texts import screen
from Sudoku.Solver.Sudoku_init import Sudoku
from Sudoku.Solver.Sudoku_init import get_values

congrats_color = False

def filler(key, mouse_coordinates, finalize):
    global congrats_color
    num_row = mouse_coordinates[1] // 50
    num_coln = mouse_coordinates[0] // 50 - 9
    if key != None:
        num_font = pygame.font.SysFont("phosphate", 40)
        num = num_font.render(str(key), True, ((255, 0, 127)), None)
        numHelper = num.get_rect()
        numHelper.center = ((num_coln * 50 + 475), (num_row * 50 + 25))
        screen.blit(num, numHelper)
    if finalize and key != None:
        buffer = get_values(num_row-1, num_coln, Sudoku)
        if key not in buffer:
            Sudoku[num_row - 1][num_coln] = key
            congrats_color = True
            # print("yes")
            # print(buffer)
            # print(num_row-1, num_coln)
        #
        if congrats_color:
            pygame.draw.rect(screen, ((11, 255, 1)), ((num_coln * 50) + 450, (num_row * 50), 50, 50), 5)
    else:
        congrats_color = False
