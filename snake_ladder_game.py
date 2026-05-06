import random

# Snakes and ladders positions
snakes = {
    16: 6,
    48: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice):
    position += dice
    if position > 100:
        return position - dice  # can't move
    
    # Check ladders
    if position in ladders:
        print(f"🚀 Ladder! Climb from {position} to {ladders[position]}")
        position = ladders[position]
    
    # Check snakes
    elif position in snakes:
        print(f"🐍 Snake! Slide from {position} to {snakes[position]}")
        position = snakes[position]
    
    return position

def play_game():
    player1 = 0
    player2 = 0
    
    print("🎲 Welcome to Snake & Ladder!")
    
    while True:
        input("\nPlayer 1 press Enter to roll dice...")
        dice = roll_dice()
        print(f"Player 1 rolled: {dice}")
        player1 = move_player(player1, dice)
        print(f"Player 1 position: {player1}")
        
        if player1 == 100:
            print("🏆 Player 1 wins!")
            break
        
        input("\nPlayer 2 press Enter to roll dice...")
        dice = roll_dice()
        print(f"Player 2 rolled: {dice}")
        player2 = move_player(player2, dice)
        print(f"Player 2 position: {player2}")
        
        if player2 == 100:
            print("🏆 Player 2 wins!")
            break

# Run the game
play_game()
