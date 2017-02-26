from utils import *

assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def crazy_triplets(values):
    return values


def naked_twins(values):
    potential_twins = [box for box in values.keys() if len(values[box]) == 2]
    naked_twins = [[box1, box2] for box1 in potential_twins for box2 in peers[box1] if
                   set(values[box1]) == set(values[box2])]

    for i in range(len(naked_twins)):
        box1 = naked_twins[i][0]
        box2 = naked_twins[i][1]
        peers1 = set(peers[box1])
        peers2 = set(peers[box2])
        peers_int = peers1.intersection(peers2)

        for peer_val in peers_int:
            if len(values[peer_val]) > 2:
                for rm_val in values[box1]:
                    values = assign_value(values, peer_val, values[peer_val].replace(rm_val, ''))
    return values


def grid_values(grid):
    if len(grid) == 81 and isinstance(grid, str):
        sudoku_dictionary = {}
        for key, value in zip(boxes, grid):
            if value is '.':
                value = '123456789'

            sudoku_dictionary = assign_value(sudoku_dictionary, key, value)

        return sudoku_dictionary
    else:
        return False


# S1
def eliminate(values):
    for k, v in values.items():
        if len(v) is 1:
            for x in peers[k]:
                if len(values[x]) > 1:
                    values = assign_value(values, x, values[x].replace(v, ''))

    return values


# S2
def only_choice(values):
    for unit in unit_list:
        for digit in cols:
            filtered_unit = [box for box in unit if digit in values[box]]
            if len(filtered_unit) == 1:
                values = assign_value(values, filtered_unit[0], digit)

    return values


def reduce_puzzle(values):
    stalled = False

    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after

        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values


# S3
# DFS
def search(values):
    values = reduce_puzzle(values)

    if values is False:
        return False

    if all(len(values[box]) == 1 for box in boxes):
        return values

    v_length, box = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)

    for value in values[box]:
        potential_v = values.copy()
        potential_v = assign_value(potential_v, box, value)
        branch_v = search(potential_v)
        if branch_v:
            return branch_v


def solve(grid):
    return search(grid_values(grid))


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
