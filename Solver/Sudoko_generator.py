from Sudoku.Solver.Sudoku_init import *

size = range(9)

Sudoku = [[0 for a in size] for b in size]


def get_new_values():
    values = [a for a in range(1, 10)]
    random.shuffle(values)
    return values


def set_values(val, row, coln):
    update_values_recors = {}
    which_value_set = {}
    set_counter = 0
    counter = 0
    row = 0
    while row < 9:
        coln = 0
        new_values = get_new_values()
        which_value_set[set_counter] = new_values
        set_counter += 1
        while coln < 9:
            checker = True
            if is_first_val:
                fill_values = values[start:]
            else:
                fill_values = values
            for update_val in new_values:
                if is_action_valid(update_val, row, coln, Sudoku):
                    Sudoku[row][coln] = update_val
                    update_values_recors[counter] = [row, coln, update_val, new_values]
                    # previous_row_coln = [row, coln, update_val]
                    is_first_val = False
                    print(np.matrix(Sudoku))
                    counter += 1
                    break
                elif row == 0 and coln == 0 and update_val == new_values[len(new_values)]:
                    print(
                        "Unsolvable Puzzle!! Ask Thomas Snyder, the best Sudoku player "
                        "in the world for help. Maybe he can solve the unsolvable. Maybe. Just Maybe.")
                    return None
                elif update_val == new_values[len(new_values)]:
                    checker = False
                    counter -= 1
                    start = update_values_recors[counter][2]
                    while start == 9:
                        counter -= 1
                        start = update_values_recors[counter][2]
                    row = update_values_recors[counter][0]
                    coln = update_values_recors[counter][1]
                    new_values = update_values_recors[counter][3]
                    break
