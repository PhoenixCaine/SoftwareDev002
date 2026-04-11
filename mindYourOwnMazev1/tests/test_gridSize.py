import pytest
from gridSize import createGrid, printGrid, selectGridSize


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

def test_printGrid_output(capsys):
    grid = [[".", "."]]
    printGrid(grid)

    captured = capsys.readouterr().out

    assert "┌" in captured
    assert "┐" in captured
    assert "└" in captured
    assert "┘" in captured
    assert ". ." in captured

def test_selectGridSize_returns_5x5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert selectGridSize() == (5, 5)

def test_selectGridSize_returns_8x8(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert selectGridSize() == (8, 8)


def test_selectGridSize_invalid_input(monkeypatch, capsys):
    inputs = iter(['3', '0', 'a', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    rows, cols = selectGridSize()
    assert (rows, cols) == (5, 5)

    captured = capsys.readouterr().out
    assert "Please enter 1 or 2." in captured
    assert "Invalid input. Please enter 1 or 2." in captured

def test_selectGridSize_whitespace(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: ' 1 ')
    assert selectGridSize() == (5, 5)