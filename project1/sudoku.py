#!/usr/bin/env python
"""
First Project on Artificial Intelligence Nanodegree at Udacity.

Student: Bruno G. Eilliar

Project Name: Solve a Sudoku with AI
"""
################
# Import Modules
################

################
# Helper Functions
################
def cross(a, b):
    """Cross('abc', 'def') will return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']"""
    return [s+t for s in a for t in b]

def grid_values(grid):
    """Return a dictionary like: {'A1': '.', 'A2': '.', 'A3': '3', ...}"""
    return dict(zip(boxes, grid))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)
    return

################
# Encoding the Board
################

rows = 'ABCDEFGHI'
cols = '123456789'

# Create label of the boxes
boxes = cross(rows, cols)
print("\nBox: \n%s" % boxes)

# Create label of the units
row_units = [cross(r, cols) for r in rows]
print("\nrow_units[0]: %s" % row_units[0])

column_units = [cross(rows, c) for c in cols]
print("\ncolumn_units[0]: %s" % column_units[0])

square_units = [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
print("\nsquare_units[0]: %s" % square_units[0])

unitlist = row_units + column_units + square_units

# Test grid_values to represent a board initial state
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
print("\nInitial board state:\n ")
display(grid_values(grid))

