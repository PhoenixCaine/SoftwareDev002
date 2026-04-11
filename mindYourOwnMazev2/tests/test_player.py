import pytest
from mindYourOwnMazeV2.player import Player

# ---------------------------
# Test for Player movement
# ---------------------------

def testPlayerMovesCorrectly():
    p = Player(1, 1)
    p.move("w", 5, 5)
    assert (p.row, p.col) == (0, 1)

    p.move("a", 5, 5)
    assert (p.row, p.col) == (0, 0)

    p.move("s", 5, 5)
    assert (p.row, p.col) == (1, 0)

    p.move("d", 5, 5)
    assert (p.row, p.col) == (1, 1)

# ---------------------------
# Test for Player boundary conditions
# ---------------------------

def testPlayerStaysInBounds():
    p = Player(0, 0)
    p.move("w", 5, 5)
    p.move("a", 5, 5)
    assert (p.row, p.col) == (0, 0)

# ---------------------------
# Test for Player health
# ---------------------------

def testPlayerHealthLoss():
    p = Player(0, 0, health=3)
    p.loseHealth()
    assert p.health == 2

# ---------------------------
# Test for Player death condition
# ---------------------------

def testPlayerDeath():
    p = Player(0, 0, health=1)
    p.loseHealth()
    assert p.isDead()
