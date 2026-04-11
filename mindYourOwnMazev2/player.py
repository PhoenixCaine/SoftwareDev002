
class Player:
    def __init__(self, row=0, col=0, health=3):
        self.row = row
        self.col = col
        self.health = health

    def move(self, direction, rows, cols):
        new_r, new_c = self.row, self.col
        if direction == "w" and self.row > 0:
            new_r-= self.row - 1
        elif direction == "s" and self.row < rows - 1:
            new_r+= self.row + 1
        elif direction == "a" and self.col > 0:
            new_c-= self.col - 1    
        elif direction == "d" and self.col < cols - 1:
            new_c+= self.col + 1
            
            self.row, self.col = new_r, new_c

    def loseHealth(self):
        self.health -= 1
        print(f"Player took damage! Health: {self.health}")

    def isDead(self):
        return self.health <= 0
    
