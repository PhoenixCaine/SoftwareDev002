import pytest
from bfs import bfs

# ---------------------------
# Test for BFS pathfinding
# ---------------------------

def test_bfs_finds_path():
    grid = [
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]
    path = bfs((0,0), (2,2), grid)
    assert path[0] == (0,0)
    assert path[-1] == (2,2)
    assert len(path) >= 3

# ---------------------------
# Test for BFS with obstacles
# ---------------------------

def test_bfs_returns_none_if_no_path():
    grid = [
        [".",".","#"],
        [".","#","#"],
        [".",".","."]
    ]
    path = bfs((0,0), (2,2), grid)
    assert path is None