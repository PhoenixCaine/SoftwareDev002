import pytest
from gridSize import createGrid

def test_createGrid_5x5():
    grid = createGrid(5, 5)
    assert len(grid) == 5
    assert len(grid[0]) == 5
    assert all(cell == "." for row in grid for cell in row)

def test_createGrid_8x8():
    grid = createGrid(8, 8)
    assert len(grid) == 8
    assert len(grid[0]) == 8
    assert all(cell == "." for row in grid for cell in row)

def test_createGrid_values_are_independent():
    grid = createGrid(3, 3)
    grid[0][0] = "X"
    assert grid[1][1] == "."