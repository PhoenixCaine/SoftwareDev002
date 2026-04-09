import pytest
from player import placePlayer, playerMovement, getPlayerInput

# ---------------------------
# Fixtures 
# ---------------------------

@pytest.fixture
def grid_and_pos():
    grid = [["." for _ in range(3)] for _ in range(3)]
    grid[1][1] = "P"
    pos = [1, 1]
    return grid, pos

# ---------------------------
# placePlayer tests
# ---------------------------

def test_place_player():
    grid = [["." for _ in range(3)] for _ in range(3)]
    pos = placePlayer(grid)

    assert pos == [0, 0]
    assert grid[0][0] == "P"

# ---------------------------
# playerMovement tests
# ---------------------------

def test_move_up(grid_and_pos):
    grid, pos = grid_and_pos
    new_pos = playerMovement(grid, pos, "w")
    assert new_pos == [0, 1]
    assert grid[0][1] == "P"
    assert grid[1][1] == "."

def test_move_down(grid_and_pos):
    grid, pos = grid_and_pos
    new_pos = playerMovement(grid, pos, "s")
    assert new_pos == [2, 1]

def test_move_left(grid_and_pos):
    grid, pos = grid_and_pos
    new_pos = playerMovement(grid, pos, "a")
    assert new_pos == [1, 0]

def test_move_right(grid_and_pos):
    grid, pos = grid_and_pos
    new_pos = playerMovement(grid, pos, "d")
    assert new_pos == [1, 2]

def test_cannot_move_outside_grid():
    grid = [["." for _ in range(3)] for _ in range(3)]
    grid[0][0] = "P"
    pos = [0, 0]

    new_pos = playerMovement(grid, pos, "w")
    assert new_pos == [0, 0]
    assert grid[0][0] == "P"

# ---------------------------
# getPlayerInput tests
# ---------------------------

def test_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "w")
    assert getPlayerInput() == "w"

def test_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "x")
    result = getPlayerInput()
    captured = capsys.readouterr()

    assert result is None
    assert "Invalid input" in captured.out