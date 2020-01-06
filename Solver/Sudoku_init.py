import random
import numpy as np
import sys
import time

start_time = time.time()

rows = range(9)
columns = range(9)
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_first_blank(Sudoku):
    for row in rows:
        for coln in columns:
            if Sudoku[row][coln] == 0:
                return (row, coln)


# def main_init():
#     values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     random.shuffle(values)
#     Sudoku = [[random.choice(values) for a in range(9)] for a in range(9)]
#     valid_init(Sudoku)
#     return Sudoku


def get_subgrid_seperators(row, coln):
    row_seperator = (0, 0)
    coln_seperator = (0, 0)
    for seperators in [3, 6, 9]:
        if 0 <= (seperators - (row + 1)) < 3:
            row_seperator = (seperators - 3, seperators)
        if 0 <= (seperators - (coln + 1)) < 3:
            coln_seperator = (seperators - 3, seperators)
    return (row_seperator, coln_seperator)

def get_values(row,coln, Sudoku):
    buffer = set()
    seperators = get_subgrid_seperators(row, coln)
    for i in range(len(Sudoku)):
        for j in range(len(Sudoku)):
            if i == row:
                buffer.add(Sudoku[i][j])
            if j == coln:
                buffer.add(Sudoku[i][j])

            if seperators[0][0] <= i < seperators[0][1] and seperators[1][0] <= j < seperators[1][1]:
                buffer.add(Sudoku[i][j])

    return buffer


def valid_value(row, coln, Sudoku, val):
    # row_values = []
    # coln_values = []
    # subgrid_values = []
    values_buffer = set()
    seperators = get_subgrid_seperators(row, coln)
    for i in range(len(Sudoku)):
        for j in range(len(Sudoku)):
            if i == row:
                if val == Sudoku[i][j]:
                    return False
                    # row_values.append(Sudoku[i][j])
            if j == coln:
                if val == Sudoku[i][j]:
                    return False
                    # coln_values.append(Sudoku[i][j])

            if seperators[0][0] <= i < seperators[0][1] and seperators[1][0] <= j < seperators[1][1]:
                if val == Sudoku[i][j]:
                    return False
                    # subgrid_values.append(Sudoku[i][j])
    # return [row_values, coln_values, subgrid_values]
    return True


def valid_init(Sudoku):
    counter = 0

    for row in rows:
        for coln in columns:
            checking_values = valid_value(row, coln, Sudoku, Sudoku[row][coln])
            cube_value = Sudoku[row][coln]
            checking_values[0].remove(cube_value), checking_values[1].remove(cube_value), checking_values[2].remove(
                cube_value)
            if cube_value in checking_values[0] or cube_value in checking_values[1] or cube_value in checking_values[2]:
                Sudoku[row][coln] = 0
                counter += 1


# def is_action_valid(val, row, coln, Sudoku):
#     checking_values = valid_value(row, coln, Sudoku)
#     if val in checking_values[0] or val in checking_values[1] or val in checking_values[2]:
#         return False
#     else:
#         return True


def solver_main(Sudoku):
    update_values_recors = {}
    counter = 0
    values.sort()
    first_blank = get_first_blank(Sudoku)
    is_first_val = True
    row = 0
    start = 0
    while row < 9:
        coln = 0
        while coln < 9:
            checker = True
            current_val = Sudoku[row][coln]
            if current_val == 0:
                if is_first_val:
                    fill_values = values[start:]
                else:
                    fill_values = values
                for update_val in fill_values:
                    if valid_value(row, coln, Sudoku, update_val):
                        Sudoku[row][coln] = update_val
                        update_values_recors[counter] = [row, coln, update_val]
                        # previous_row_coln = [row, coln, update_val]
                        is_first_val = False
                        # print(np.matrix(Sudoku))
                        counter += 1
                        break
                    elif update_val == 9 and row == first_blank[0] and coln == first_blank[1]:
                        print(
                            "Unsolvable Puzzle!! Ask Thomas Snyder, the best Sudoku player "
                            "in the world for help. Maybe he can solve the unsolvable. Maybe. Just Maybe.")
                        return None
                    elif update_val == 9:
                        checker = False
                        counter -= 1
                        start = update_values_recors[counter][2]
                        while start == 9:
                            Sudoku[update_values_recors[counter][0]][update_values_recors[counter][1]] = 0
                            counter -= 1
                            if counter == -1:
                                print(
                                    "Unsolvable Puzzle!! Ask Thomas Snyder, the best Sudoku player "
                                    "in the world for help. Maybe he can solve the unsolvable. Maybe. Just Maybe.")
                                return None
                            start = update_values_recors[counter][2]
                        row = update_values_recors[counter][0]
                        coln = update_values_recors[counter][1]
                        Sudoku[row][coln] = 0
                        is_first_val = True
                        break
                        # solver_main(Sudoku, previous_row_coln[2])
            if checker: coln += 1
        if checker: row += 1

    print("sUccEss")
    return Sudoku


# Sudoku = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]


def main():
    # random.shuffle(values)
    # Sudoku = [[random.choice(values) for a in range(9)] for b in range(9)]
    # valid_init(Sudoku)

    # Sudoku = [[7, 2, 0, 0, 0, 0, 0, 0, 0,],
    # [9 ,0 ,0, 0, 0, 8, 3, 4, 0],
    # [0, 0, 8, 0, 3, 0, 6, 5, 9],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 9, 0, 0, 0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0, 4, 0, 0, 0],
    # [0, 0, 0, 0, 5, 6, 0, 0, 0]]
    Sudoku = [[0, 0, 9, 0, 0, 7, 4, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 3, 2],
              [0, 8, 0, 3, 0, 0, 0, 0, 0],
              [0, 2, 0, 8, 4, 0, 0, 0, 6],
              [8, 0, 0, 0, 0, 0, 0, 0, 1],
              [9, 0, 0, 0, 1, 5, 0, 7, 0],
              [0, 0, 0, 0, 0, 6, 0, 9, 0],
              [5, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 4, 2, 0, 0, 5, 0, 0]]
    solver_main(Sudoku)
    print(np.matrix(Sudoku))


if __name__ == "__main__":
    main()
    print(time.time() - start_time)
