# Utility

rows = 'ABCDEFGHI'
cols = '123456789'


# returns Sudoku box names
def cross(row, column):
    return [r + c for r in row for c in column]


# All boxes in Sudoku
boxes = cross(rows, cols)

# Unit ref
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
lr_dia_units = [[rows[i] + cols[i] for i in range(len(rows))]]
rl_dia_units = [[rows[i] + cols[::-1][i] for i in range(len(rows))]]

# merge all units
unit_list = row_units + column_units + square_units + lr_dia_units + rl_dia_units

# Unit & Peer info dictionaries
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


# Presentation util
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
