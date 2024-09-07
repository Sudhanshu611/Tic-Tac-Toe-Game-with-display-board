import random

def display_board():
    print("\nCurrent Board:")
    print('|',boardList[0],'|',boardList[1],'|',boardList[2],'|')
    print('|',boardList[3],'|',boardList[4],'|',boardList[5],'|')
    print('|',boardList[6],'|',boardList[7],'|',boardList[8],'|')
    print("\n")
    
def validate_position(position):
    if not position.isdigit():
        print("Use Digits only.")
        return False
    elif len(position)>1:
        print("Type single digit only.")
        return False
    elif int(position) in oppSelections:
        print("Postion already taken")
        return False
    elif int(position) in userSelections:
        print("Postion already taken")
        return False
    elif 1 > int(position) or int(position) > 9:
        print("Select between 1-9 only.")
        return False
    return True

def game_checker():  
    global gameStart
    win_conditions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal top-left to bottom-right
        (2, 4, 6)   # Diagonal top-right to bottom-left
    ]
    
    for condition in win_conditions:
        if all(boardList[pos] == usersOption for pos in condition):
            print("""
|---------------|
|   You Win!!   |
|---------------|
""")
            gameStart = False
            return False
        elif all(boardList[pos] == oppOption for pos in condition):
            print("""
|--------------------|
|   Opponent Wins!!  |
|--------------------|
""")
            gameStart = False
            return False

    if "_" not in boardList:  # Draw condition
        print("""
|----------------|
|  It's a Draw!  |
|----------------|
""")
        gameStart = False
        return False

    return True  # Continue playing if no win or draw


def restart_game():
    global boardList, userSelections, oppSelections, gameStart
    boardList = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    userSelections = []
    oppSelections = []
    gameStart = True

usersOption = ''
oppOption = ''

boardList = ['_','_','_',
             '_','_','_',
             '_','_','_',]
game = True
while game:
    print("""
Welcome to Tic-Tac-Toe
----------------------
Choose X or 0:
1. X
2.0
""")
    X_or_0 = (input("\nType your number here for selection: "))
        
    while True:
        if len((X_or_0)) > 1 or int(X_or_0) < 1 or int(X_or_0) > 2:
            print("Select 1 or 2 only.")
            continue
        elif not X_or_0.isdigit():
            print("Select 1 or 2 only.")
            continue
        elif int(X_or_0) == 1:
            usersOption = 'X'
            oppOption = '0'
            break
        elif int(X_or_0) == 2:
            usersOption = '0'
            oppOption = 'X'
            break   
        
    def opp_selection():
        global userSelections
        global oppSelections
    
        while True:
            opp_position = random.choice([1,2,3,4,5,6,7,8,9])
            if not (opp_position) in userSelections:
               if not (opp_position) in oppSelections:
                    oppSelections.append(int(opp_position))
                    opp_position = int(opp_position) -1
                    boardList[opp_position] = oppOption
               
                    break
            else:
                    continue
            
    
    
# Main Game stopper
    gameStart = True

    userSelections = []
    oppSelections = []

    while gameStart:
    
        print("Your Position:",userSelections)
        print("Opponents Position:",oppSelections)
    
        if game_checker() == True:
            position = input("Type your position here 1-9: ")
            if not validate_position(position):
                continue
            if position.isdigit():
                userSelections.append(int(position))
                position = int(position) - 1
                boardList[position] = usersOption
        
        if not game_checker():
            break        
        
        opp_selection()
        display_board()
        
        if not game_checker():
            break
        
        
   
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again.isalpha() or len(play_again) > 1 or play_again not in ['y','n']:
            print("Use 'y' for yes or 'n' for no.")
            continue
        elif play_again == 'y':
            restart_game()
            break
        if play_again == 'n':
            print("Goodbye!")
            game = False
            break
  
    

