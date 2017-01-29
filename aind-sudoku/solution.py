assignments = []
import collections
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    for unit in unitlist:
       bb2 = [values[box] for box in unit if len(values[box])==2]
       counter = collections.Counter(bb2)      
       twins = [v for v, n in counter.items() if n==2]
       for twin in twins:
           for box in unit:
               if values[box] != twin and len(values[box]) != 1:
                   new_value = values[box]
                   for digit in twin:
                       new_value = new_value.replace(digit, '')
                       assign_value(values, box, new_value)
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'
n=len(rows)
boxes = cross(rows, cols)
diagonal_units = [[rows[i]+cols[n-i-1] for i in range(len(rows))],[rows[i]+cols[i] for i in range(len(rows))]]
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units+diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    s = dict(zip(boxes,grid))
    for i in range(len(s)):
        if s[boxes[i]]=='.':
            s[boxes[i]]="123456789"
    return s

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    v=[]
    for i in range(len(values)):
        a = values[boxes[i]]
        if len(a)==1:
            v.append(boxes[i])
    for i in v:
        a = values[i]
        for j in peers[i]:
            values[j]=values[j].replace(a,'')
    return values

def only_choice(values):
    new_values = values.copy()  # note: do not modify original values
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                new_values[dplaces[0]] = digit
    # unable to figure out problem with the code below
    """v=[]
    for i in range(len(values)):
        a = values[boxes[i]]
        if len(a)==1:
            v.append(boxes[i])
    for i in v:
        a = values[i]
        for j in peers[i]:
            values[j]=values[j].replace(a,'')
    for square in square_units:
        c=[]
        b=[]
        for i in range(0,10):
            c.append(0)
            b.append("")
        for cells in square:
            string = new_values[cells]
            for digit in string:
                digit = int(digit)
                if c[digit]!=1:
                    b[digit]=cells
                c[digit]=c[digit]+1
        for i in range(0,10):
            if c[i]==1:
                new_values[b[i]]=str(i)"""
        
    return new_values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

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
