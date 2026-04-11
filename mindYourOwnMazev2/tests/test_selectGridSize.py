import pytest
from mindYourOwnMazeV2.gridSize import selectGridSize

# ---------------------------
# Test for selectGridSize function with 5x5 option
# ---------------------------

def test_selectGridSize_5x5(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert selectGridSize() == (5, 5)

# ---------------------------
# Test for selectGridSize function with 8x8 option
# ---------------------------

def test_selectGridSize_8x8(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert selectGridSize() == (8, 8)

# ---------------------------
# Test for selectGridSize function with invalid input followed by valid input
# ---------------------------

def test_selectGridSize_invalid_then_valid(monkeypatch):
    inputs = iter(["x", "3", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert selectGridSize() == (5, 5)