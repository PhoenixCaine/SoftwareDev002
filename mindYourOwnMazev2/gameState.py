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

    def player_on_item(self):
        return (self.player.row, self.player.col) == self.item_pos

    def player_on_trap(self):
        return (self.player.row, self.player.col) in self.traps