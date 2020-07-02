import random

playground = ["A","1","2","3","4","5","6","7","8","9" ]
player = ["X", "O"]
currentPlayer = "X"
modus = None

def printPlayground():
    print(playground[1] + "|" + playground[2] + "|" + playground[3])
    print(playground[4] + "|" + playground[5] + "|" + playground[6])
    print(playground[7] + "|" + playground[8] + "|" + playground[9])


def playerInput():
    while True:
        print()
        print("{} is on move".format(currentPlayer))
        playIn = input("Choose the field: ")   
        if playIn == 'q':
            return 'q'        
        try:
            playIn = int(playIn)
        except ValueError:
            print("Please use only values between 1 and 9")
        else:
            if playIn >= 1 and playIn < 10:
                if playground[playIn] == 'X' or playground[playIn] == 'O':
                    print("The field is already occupied.")
                else:
                    return playIn
            else:
                print("Only numbers between 1 and 9!")

def changePlayer():
    global currentPlayer
    global modus
    if modus == 'p':
        if currentPlayer == player[0]:
            currentPlayer = player[1]
        else:
            currentPlayer = player[0]
    else:
        if currentPlayer == 'C':
            currentPlayer = 'P'
        else:
            currentPlayer = 'C'

#return True if game ended
def gameEnd():
    for i in playground:
        if i.isnumeric():
            return False
    return True

def setStone(input):
    global currentPlayer

    if currentPlayer == player[0]:
        playground[input] = 'X'
    elif currentPlayer == 'C':
        playground[input] = 'C'
    else:
        playground[input] = 'O'

def checkForWin():
    if playground[1] == playground[2] and playground[2] == playground[3]:
        return playground[2]
    elif playground[4] == playground[5] and playground[5] == playground[6]:
        return playground[5]
    elif playground[7] == playground[8] and playground[8] == playground[9]:
        return playground[8]
    elif playground[1] == playground[4] and playground[4] == playground[7]:
        return playground[4]
    elif playground[2] == playground[5] and playground[5] == playground[8]:
        return playground[5]
    elif playground[3] == playground[6] and playground[6] == playground[9]:
        return playground[6]
    elif playground[1] == playground[5] and playground[5] == playground[9]:
        return playground[5]
    elif playground[3] == playground[5] and playground[5] == playground[7]:
        return playground[5]

def gameLoop():
    global modus
    global currentPlayer
    activ = True
    modus = input("Chose the modus - 'c' for against computer or 'p' for 2 players: ")
    if modus == 'c':
            currentPlayer = 'C'

    while activ:
        printPlayground()
        if currentPlayer == 'C':
            playground_KI = []
            for field in playground:
                if field != 'X' and field != 'C' and field != 'A':
                    playground_KI += field
            setStone(int(random.choice(playground_KI)))
            print()
            print("C has placed.")
        else:
            inputPlayer = playerInput()
            if inputPlayer == 'q':
                activ = False
            else:
                setStone(inputPlayer)

        if gameEnd():
            printPlayground()
            print("Game over. Egality!")
            activ = False
        win = checkForWin()
        if win:
            printPlayground()
            print("{} won the game.".format(win))
            activ = False
        changePlayer()

if __name__ == "__main__":
    gameLoop()