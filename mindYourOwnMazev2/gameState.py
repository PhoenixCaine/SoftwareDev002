class GameState:
    def __init__(self, grid, player, item_pos, traps):
        self.grid = grid
        self.player = player
        self.item_pos = item_pos
        self.traps = traps
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.running = True
        self.reveal = False
        self.revealedTraps = set()

# --- Health based on grid size ---
        if (self.rows, self.cols) == (5, 5):
            self.health = 3
        elif (self.rows, self.cols) == (8, 8):
            self.health = 5
        else:
            # rule added for future grid sizes
            self.health = max(1, (self.rows + self.cols) // 4)


    def player_on_item(self):
        return (self.player.row, self.player.col) == self.item_pos

    def player_on_trap(self):
        return (self.player.row, self.player.col) in self.traps