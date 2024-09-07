import random

usersOption = ''
oppOption = ''

boardList = ['_','_','_',
             '_','_','_',
             '_','_','_',]

# Choose b/w X or 0
print("""
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
               boardList[int(opp_position)-1] = oppOption
               oppSelections.append(int(opp_position))
               break
            else:
                continue
        else:
            continue

def game_checker():  
    global gameStart
    if (boardList[0] == boardList[4] == boardList[8] == usersOption) or (boardList[2] == boardList[4] == boardList[6] == usersOption) or (boardList[0] == boardList[1] == boardList[2] == usersOption) or (boardList[0] == boardList[3] == boardList[6] == usersOption) or (boardList[6] == boardList[7] == boardList[8] == usersOption) or (boardList[2] == boardList[5] == boardList[8] == usersOption):
        print("""
|               |
|   You Win!!   |
|               |
""")
        gameStart = False
    elif (boardList[0] == boardList[4] == boardList[8] == oppOption) or (boardList[2] == boardList[4] == boardList[6] == oppOption) or (boardList[0] == boardList[1] == boardList[2] == oppOption) or (boardList[0] == boardList[3] == boardList[6] == oppOption) or (boardList[6] == boardList[7] == boardList[8] == oppOption) or (boardList[2] == boardList[5] == boardList[8] == oppOption):
        print("""
|                    |
|   Opponent Win!!   |
|                    |
""")
        gameStart = False
    else:
        return True
    
# Main Game stopper
gameStart = True

userSelections = []
oppSelections = []

while gameStart:
    
    print('|',boardList[0],'|',boardList[1],'|',boardList[2],'|')
    print('|',boardList[3],'|',boardList[4],'|',boardList[5],'|')
    print('|',boardList[6],'|',boardList[7],'|',boardList[8],'|')
    
    game_checker()
    
    print(userSelections)
    print(oppSelections)
    
    if game_checker() == True:
        position = input("Type your position here 1-9: ")
        if not position.isdigit():
            print("Use Digits only.")
            continue
        elif len(position)>1:
            print("Type single digit only.")
            continue
        elif int(position) in oppSelections:
            print("Postion already taken")
            continue
        elif int(position) in userSelections:
            print("Postion already taken")
            continue
        elif 1 > int(position) or int(position) > 9:
            print("Select between 1-9 only.")
            continue
        elif position.isdigit():
            userSelections.append(int(position))
            boardList[int(position)-1] = usersOption
            opp_selection()
    else: gameStart = False