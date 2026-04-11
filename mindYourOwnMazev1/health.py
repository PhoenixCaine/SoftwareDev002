lives = 3

def loseLife():
    global lives
    lives -= 1
    print(f"Player lost a life. Lives remaining: {lives}")

def checkGameOver():
    if lives <= 0:
        print("Game Over! You have no lives left.")
        return True
    return False

def resetLives():
    global lives
    lives = 3   

def showLives():
    print(f"Lives remaining: {lives}")