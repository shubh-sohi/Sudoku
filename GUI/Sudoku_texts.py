import pygame

screen = pygame.display.set_mode((1000, 650))


def helper_text():
    helper_font = pygame.font.SysFont("phosphate", 30)
    helper = helper_font.render("Available numbers ", True, ((0, 0, 160)), None)
    helperRect = helper.get_rect()
    helperRect.center = (220, 570)
    screen.blit(helper, helperRect)


def sudoku_text():
    logo_font = pygame.font.SysFont("phosphate", 100)
    logo = logo_font.render("Sudoku", True, ((0, 0, 160)), None)
    logoRect = logo.get_rect()
    logoRect.center = (220, 80)
    screen.blit(logo, logoRect)


def solve_text():
    logo_font = pygame.font.SysFont("phosphate", 50)
    logo = logo_font.render("Solve Sudoku", True, ((0, 0, 160)), None)
    logoRect = logo.get_rect()
    logoRect.center = (220, 180)
    screen.blit(logo, logoRect)


def new_puzzle_text():
    logo_font = pygame.font.SysFont("phosphate", 50)
    logo = logo_font.render("New Sudoku", True, ((0, 0, 160)), None)
    logoRect = logo.get_rect()
    logoRect.center = (220, 260)
    screen.blit(logo, logoRect)


def reset_text():
    logo_font = pygame.font.SysFont("phosphate", 50)
    logo = logo_font.render("Reset", True, ((0, 0, 160)), None)
    logoRect = logo.get_rect()
    logoRect.center = (220, 460)
    screen.blit(logo, logoRect)


def make_my_own_sudoku_text():
    logo_font = pygame.font.SysFont("phosphate", 40)
    logo = logo_font.render("Make my own", True, ((0, 0, 160)), None)
    logoRect = logo.get_rect()
    logoRect.center = (220, 340)
    screen.blit(logo, logoRect)
    helper_font = pygame.font.SysFont("phosphate", 50)
    helper = helper_font.render("Sudoku ", True, ((0, 0, 160)), None)
    helperRect = helper.get_rect()
    helperRect.center = (220, 380)
    screen.blit(helper, helperRect)

def text_main():
    helper_text()
    sudoku_text()
    solve_text()
    new_puzzle_text()
    reset_text()
    make_my_own_sudoku_text()
