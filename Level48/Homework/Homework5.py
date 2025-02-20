def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if rules[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
