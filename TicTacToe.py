import random
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (210, 210, 210)
OFFSET = 100

class Player:
    def __init__(self, symbol):
        self.symbol = symbol


def printPlayground(board):
    print(" " + board[1-1] + "|" + board[2-1] + "|" + board[3-1])
    print(" " + board[4-1] + "|" + board[5-1] + "|" + board[6-1])
    print(" " + board[7-1] + "|" + board[8-1] + "|" + board[9-1])


def playerInput(board, currentPlayer):
    while True:
        print("Player {} is on move".format(currentPlayer.symbol))
        position = input("Choose the field: ")
        if position == 'q':
            return 'q'
        try:
            position = int(position)
        except ValueError:
            print("Please use numbers")
        else:
            if position >= 1 and position < 10:
                position -= 1
                if not board[position] == ' ':
                    print("The field is already occupied.")
                else:
                    return position
            else:
                print("Only numbers between 1 and 9!")


def changePlayer(current_player, player_1, player_2):
    if current_player == player_1:
        return player_2
    else:
        return player_1


def gameEnd(board):
    for i in board:
        if i == ' ':
            return False
    return True


def setStone(input, board, current_player):
    board[input] = current_player.symbol


def checkForWin(board):
    if board[1-1] == board[2-1] and board[2-1] == board[3-1] and board[1-1] != ' ':
        return True, board[1-1]
    elif board[4-1] == board[5-1] and board[5-1] == board[6-1] and board[4-1] != ' ':
        return True, board[4-1]
    elif board[7-1] == board[8-1] and board[8-1] == board[9-1] and board[7-1] != ' ':
        return True, board[7-1]
    elif board[1-1] == board[4-1] and board[4-1] == board[7-1] and board[1-1] != ' ':
        return True, board[1-1]
    elif board[2-1] == board[5-1] and board[5-1] == board[8-1] and board[2-1] != ' ':
        return True, board[2-1]
    elif board[3-1] == board[6-1] and board[6-1] == board[9-1] and board[3-1] != ' ':
        return True, board[3-1]
    elif board[1-1] == board[5-1] and board[5-1] == board[9-1] and board[1-1] != ' ':
        return True, board[1-1]
    elif board[3-1] == board[5-1] and board[5-1] == board[7-1] and board[3-1] != ' ':
        return True, board[3-1]
    return None, None


def play_again():
    print("Wanna play again? (y or n)")
    return input().lower().startswith('y')


def copy_board(board):
    return baord.copy()


def choose_random_move(board, list_moves):
    for i in list_moves:
        if board[i] != ' ':
            list_moves.remove(i)
    if len(list_moves) != 0:
        return random.choice(list_moves)
    else:
        return None

# simple AI to compute the move
def get_ai_move(board, player, oponent):
    # 1. check for a winning move
    for i in range(0, 9):
        if board[i] == ' ':
            copy = copy_board(board)
            setStone(i, copy, player)
            if checkForWin(copy, player):
                return i
    # 2. check to prevent a lose
    for i in range(0, 9):
        if board[i] == ' ':
            copy = copy_board(board)
            setStone(i, copy, oponent)
            if checkForWin(copy, oponent):
                return i

    # 3. if possible place symbol in corner
    move_pos = choose_random_move(board, [0, 2, 6, 8])
    if move_pos != None:
        return move_pos
    # 4. if possible place symbol in center
    move_pos = choose_random_move(board, [4])
    if move_pos != None:
        return move_pos
    # 5. if possible place symbol in side
    move_pos = choose_random_move(board, [1, 3, 5, 7])
    if move_pos != None:
        return move_pos


def best_move(board, ai):
    # AI to make its turn
    best_score = -1000
    move = 0
    for i in range(len(board)):
        # is the spot available?
        if board[i] == ' ':
            board[i] = ai.symbol
            score = minimax(board, 2, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


def minimax(board, depth, is_maximizer):
    scores = [0, 1, -1]
    win, player = checkForWin(board)
    if win:
        return scores[1] if player == 'O' else scores[2]
    if gameEnd(board):
        return scores[0]
        # if it's not a final state
    if is_maximizer:
        best_value = -1000
        for i in range(len(board)):
            # is the spot available?
            if board[i] == ' ':
                board[i] = 'O'
                value = minimax(board, depth + 1, False)
                # Delete tested spot ... you could also do a copy of the board
                board[i] = ' '
                best_value = max(value, best_value)
        return best_value
    else:
        best_value = 1000
        for i in range(len(board)):
            # is the spot available?
            if board[i] == ' ':
                board[i] = 'X'
                value = minimax(board, depth + 1, True)
                board[i] = ' '
                best_value = min(value, best_value)
        return best_value


def gameLoop():
    screen = ui_setup()
    while True:
        # Reset the board
        board = [' '] * 9
        draw_empty_board(screen, board)
        player_1 = Player('X')
        player_2 = Player('O')      # AI
        current_player = player_1
        gameOver = False
        # try:
        #     modus = str(input(
        #         "Chose the modus - 'c' for against computer or 'p' for 2 players: ").lower())
        #     if not modus.startswith(('c', 'p')):
        #         continue
        # except ValueError:
        #     print("Please ty again")
        #     continue
        # if modus == 'c':
        #     print("Computer is Player O")
        # try:
        #     start_player = str(
        #         input("Who want`s to start? (X or O): ").upper())
        #     if not start_player.startswith(('X', 'O')):
        #         continue
        # except ValueError:
        #     print("Please try again")
        #     continue
        # if start_player == 'X':
        #     current_player = player_1
        # else:
        #     current_player = player_2

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                # printPlayground(board)
                # print()
                # #Check if AI is selected
                # if current_player == player_2 and modus == 'c':
                #     print("Computer is on move")
                #     setStone(best_move(board, current_player),
                #             board, current_player)
                # else:
                    # inputPlayer = playerInput(board, current_player)
                    # if inputPlayer == 'q':
                    #     break
                    # else:
                    #     setStone(inputPlayer, board, current_player)
                if event.type == pygame.MOUSEBUTTONDOWN and current_player == player_1:
                    posx, posy = event.pos
                    if posx >= 0 and posx < OFFSET and posy >= 0 and posy < OFFSET:
                        place = 0
                    if posx >= OFFSET and posx < OFFSET * 2 and posy >= 0 and posy < OFFSET:
                        place = 1
                    if posx >= OFFSET * 2 and posx < OFFSET * 3 and posy >= 0 and posy < OFFSET:
                        place = 2
                    if posx >= 0 and posx < OFFSET and posy >= OFFSET and posy < OFFSET * 2:
                        place = 3
                    if posx >= OFFSET and posx < OFFSET * 2 and posy >= OFFSET and posy < OFFSET * 2:
                        place = 4
                    if posx >= OFFSET * 2 and posx < OFFSET * 3 and posy >= OFFSET and posy < OFFSET * 2:
                        place = 5
                    if posx >= 0 and posx < OFFSET and posy >= OFFSET * 2 and posy < OFFSET * 3:
                        place = 6
                    if posx >= OFFSET and posx < OFFSET * 2 and posy >= OFFSET * 2 and posy < OFFSET * 3:
                        place = 7
                    if posx >= OFFSET * 2 and posx < OFFSET * 3 and posy >= OFFSET * 2 and posy < OFFSET * 3:
                        place = 8
                    
                    if not board[place] == ' ':
                        continue
                    setStone(place, board, current_player)
                    win, player = checkForWin(board)
                    if win:
                        print("{} won the game.".format(player))    
                        show_message(screen, player + "WON!")
                        gameOver = True
                    elif gameEnd(board):
                        gameOver = True
                        show_message(screen, "Egality")
                        print("p")
                    printPlayground(board)
                    draw_board(screen, board)
                    current_player = changePlayer(current_player, player_1, player_2)
            
            if current_player == player_2 and not gameOver:
                setStone(best_move(board, current_player), board, current_player)
                win, player = checkForWin(board)
                if win:
                    print("{} won the game.".format(player))
                    show_message(screen, player + " WON!")
                    gameOver = True
                elif gameEnd(board):
                    gameOver = True
                    show_message(screen, "Egality")
                draw_board(screen, board)
                current_player = changePlayer(current_player, player_1, player_2)



def ui_setup():
    pygame.init()
    height = 300
    width = 300
    pygame.display.set_caption('TicTacToe')
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    return screen

def draw_board(screen, board):
    myfont = pygame.font.SysFont("monospace", 100)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 4)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 4)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 4)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 4)

    if board:

        for i in range(len(board)):
            if i < 3:
                posx = i * 100 + 25
                posy = 25
            elif 3 <= i < 6 :
                posx = (i - 3) * 100 + 25
                posy = 125
            elif 6 <= i < 9:
                posx = (i - 6) * 100 + 25
                posy = 225

            if board[i] == 'X':
                label = myfont.render("X", 1, BLACK)
                screen.blit(label, (posx, posy))
            elif board[i] == 'O':
                label = myfont.render("O", 1, GREY)
                screen.blit(label, (posx, posy))

    pygame.display.flip()

def draw_empty_board(screen, board):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 4)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 4)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 4)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 4)
    pygame.display.flip()

def show_message(screen, message):
    screen.fill(WHITE)
    myfont = pygame.font.SysFont("monospace", 60)
    label = myfont.render(message, 1, BLACK)
    screen.blit(label, (80, 120))
    pygame.display.flip()
    pygame.time.delay(2000)

if __name__ == "__main__":
    gameLoop()
