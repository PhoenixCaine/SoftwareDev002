import pytest
from player import Player
from gameState import GameState

# ---------------------------
# Test for GameState player interactions
# ---------------------------

def make_state():
    grid = [["." for _ in range(3)] for _ in range(3)]
    p = Player(1, 1)
    item = (2, 2)
    traps = {(0, 2), (2, 0)}
    return GameState(grid, p, item, traps)

# ---------------------------
# Test for player on item
# ---------------------------

def test_player_on_item():
    gs = make_state()
    gs.player.row, gs.player.col = (2, 2)
    assert gs.player_on_item()

# ---------------------------
# Test for Player on trap
# ---------------------------

def test_player_on_trap():
    gs = make_state()
    gs.player.row, gs.player.col = (0, 2)
    assert gs.player_on_trap()

# ---------------------------
# Test for Player not on trap or item
# ---------------------------

def test_player_not_on_trap_or_item():
    gs = make_state()
    gs.player.row, gs.player.col = (1, 1)
    assert not gs.player_on_item()
    assert not gs.player_on_trap()