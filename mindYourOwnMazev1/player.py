
player = "P"

def placePlayer(grid):
    player_pos = [0, 0]
    grid[player_pos[0]][player_pos[1]] = "P"
    return player_pos


def playerMovement(grid, player_pos, direction):
    rows = len(grid)
    cols = len(grid[0])

    r, c = player_pos

    new_r, new_c = r, c

    if direction == "w" and r > 0:
        new_r -= 1
    elif direction == "s" and r < rows - 1:
        new_r += 1
    elif direction == "a" and c > 0:
        new_c -= 1
    elif direction == "d" and c < cols - 1:
        new_c += 1

    # Only update if the position changed
    if (new_r, new_c) != (r, c):
        grid[r][c] = "."
        grid[new_r][new_c] = "P"
        player_pos[0], player_pos[1] = new_r, new_c

    return player_pos


def getPlayerInput():
    direction = input("Enter direction (w, s, a, d): ").lower()
    if direction in ["w", "a", "s", "d"]:
        return direction
    else:
        print("Invalid input.")
        return None