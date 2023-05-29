import os
import copy
import random

def actions(board):
    #takes in the board as an array and returns set of moves (legal and illegal) as a list
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!= ".":
                movesPiece(board[i][j], i, j, board, moves)
    return moves 

def movesPiece(pieceName, startY, startX, board, moves):
    # call appropriate function to get moves for each type of piece
    if "K" in pieceName:
        movesKing(startY, startX, board, moves)
    if pieceName == "wP":
        movesWhitePawn(startY, startX, board, moves)
    if pieceName == "bP":
        movesBlackPawn(startY, startX, board, moves)
    if "N" in pieceName:
        movesKnight(startY, startX, board, moves)
    if "R" in pieceName:
        movesRook(startY, startX, board, moves)
    if "B" in pieceName:
        movesBishop(startY, startX, board, moves)
    if "Q" in pieceName:
        movesQueen(startY, startX, board, moves)

def movesKing(startY, startX, board, moves):
    if isOnBoard(startY+1, startX) and containsPiece(startY+1, startX, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY+1+1))
    if isOnBoard(startY-1, startX) and containsPiece(startY-1, startX, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY-1+1))
    if isOnBoard(startY, startX+1) and containsPiece(startY, startX+1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY+1))
    if isOnBoard(startY, startX-1) and containsPiece(startY, startX-1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY+1))

    #diagonals
    if isOnBoard(startY+1, startX+1) and containsPiece(startY+1, startX+1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY+1+1))
    if isOnBoard(startY-1, startX+1) and containsPiece(startY-1, startX+1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY-1+1))

    if isOnBoard(startY-1, startX-1) and containsPiece(startY-1, startX-1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY-1+1))
    if isOnBoard(startY+1, startX-1) and containsPiece(startY+1, startX-1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY+1+1))
    #TODO implement castling

def movesWhitePawn(startY, startX, board, moves):
    #move foward 2 squares if no piece and first move
    if startY == 1 and containsPiece(startY+1, startX, board) == "False" and containsPiece(startY+2, startX, board) == "False":
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY+2+1))

    #move foward 1 sq if no piece
    if isOnBoard(startY+1, startX) and containsPiece(startY+1, startX, board) == "False":
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY+1+1))

    #move foward diag if opponent piece
    if isOnBoard(startY+1, startX+1) and containsPiece(startY+1, startX+1, board)!= board[startY][startX][0] and containsPiece(startY+1, startX+1, board) != "False": 
         moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY+1+1))
    if isOnBoard(startY+1, startX-1) and containsPiece(startY+1, startX-1, board)!= board[startY][startX][0] and containsPiece(startY+1, startX-1, board) != "False":
         moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY+1+1))
    
def movesBlackPawn(startY, startX, board, moves):
    #move foward 2 squares if no piece and first move
    if startY == 6 and containsPiece(startY-1, startX, board) =="False" and containsPiece(startY-2, startX, board) == "False":
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY-2+1))

    #move foward 1 sq if no piece
    if isOnBoard(startY-1, startX) and containsPiece(startY-1, startX, board) == "False":
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(startY-1+1))

    #move foward diag if opponent piece
    if isOnBoard(startY-1, startX+1) and containsPiece(startY-1, startX+1, board)!= board[startY][startX][0] and containsPiece(startY-1, startX+1, board) != "False":
         moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY-1+1))
    if isOnBoard(startY-1, startX-1) and containsPiece(startY-1, startX-1, board)!= board[startY][startX][0] and containsPiece(startY-1, startX-1, board) != "False":
         moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY-1+1))

def containsPiece(Y, X, board): 
    if board[Y][X] == ".":
        return "False"
    elif "b" in board[Y][X]:
        return "b"
    elif "w" in board[Y][X]:
        return "w"

def movesKnight(startY, startX, board, moves):
    if isOnBoard(startY+2, startX+1) and containsPiece(startY+2, startX+1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY+2+1))
    if isOnBoard(startY+2, startX-1) and containsPiece(startY+2, startX-1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY+2+1))
    if isOnBoard(startY-2, startX+1) and containsPiece(startY-2, startX+1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+1) + str(startY-2+1))
    if isOnBoard(startY-2, startX-1) and containsPiece(startY-2, startX-1, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-1) + str(startY-2+1))
    if isOnBoard(startY+1, startX+2) and containsPiece(startY+1, startX+2, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+2) + str(startY+1+1))
    if isOnBoard(startY-1, startX+2) and containsPiece(startY-1, startX+2, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX+2) + str(startY-1+1))
    if isOnBoard(startY+1, startX-2) and containsPiece(startY+1, startX-2, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-2) + str(startY+1+1))
    if isOnBoard(startY-1, startX-2) and containsPiece(startY-1, startX-2, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX-2) + str(startY-1+1))
    return

def movesBishop(startY, startX, board, moves):
    Y = startY+1
    X = startX+1
    while isOnBoard(Y, X) and containsPiece(Y, X, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(Y+1))
        if containsPiece(Y, X, board) != "False":
            break
        Y+=1
        X+=1

    Y = startY+1
    X = startX-1
    while isOnBoard(Y, X) and containsPiece(Y, X, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(Y+1))
        if containsPiece(Y, X, board) != "False":
            break
        Y+=1
        X-=1

    Y = startY-1
    X = startX-1
    while isOnBoard(Y, X) and containsPiece(Y, X, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(Y+1))
        if containsPiece(Y, X, board) != "False":
            break
        Y-=1
        X-=1

    Y = startY-1
    X = startX+1
    while isOnBoard(Y, X) and containsPiece(Y, X, board) != board[startY][startX][0]:
        moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(Y+1))
        if containsPiece(Y, X, board) != "False":
            break
        Y-=1
        X+=1
    

def movesRook(startY, startX, board, moves):
    #moving left on board
    for X in range(startX-1,-1,-1):
        if isOnBoard(startY, X) and containsPiece(startY, X, board) != board[startY][startX][0]:
            moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(startY+1))
        if containsPiece(startY, X, board) != "False":
            break

    #moving right on board
    for X in range(startX+1,8,1):
        if isOnBoard(startY, X) and containsPiece(startY, X, board) != board[startY][startX][0]:
            moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(X) + str(startY+1))
        if containsPiece(startY, X, board) != "False":
            break

    #moving down board
    for Y in range(startY+1,8,1):
        if isOnBoard(Y, startX) and containsPiece(Y, startX, board) != board[startY][startX][0]:
            moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(Y+1))
        if containsPiece(Y, startX, board) != "False":
            break

    #moving up board
    for Y in range(startY-1,-1,-1):
        if isOnBoard(Y, startX) and containsPiece(Y, startX, board) != board[startY][startX][0]:
            moves.append(getCharIndex(startX)+str(startY+1)+ " " + getCharIndex(startX) + str(Y+1))
        if containsPiece(Y, startX, board) != "False":
            break
    
def movesQueen(startY, startX, board, moves):
    movesRook(startY, startX, board, moves)
    movesBishop(startY, startX, board, moves)

def isOnBoard(Y, X):
    if Y > -1 and Y < 8 and X > -1 and X < 8:
        return True
    else:
        return False

def getCharIndex(int):
    if int == 0:
        return "A"
    if int == 1:
        return "B"
    if int == 2:
        return "C"
    if int == 3:
        return "D"
    if int == 4:
        return "E"
    if int == 5:
        return "F"
    if int == 6:
        return "G"
    if int == 7:
        return "H"
    
def getIntIndex(str):
    if str == "A":
        return 0
    if str == "B":
        return 1
    if str == "C":
        return 2
    if str == "D":
        return 3
    if str == "E":
        return 4
    if str == "F":
        return 5
    if str == "G":
        return 6
    if str == "H":
        return 7

def switchTurn(turn, turn1):
    #switches to the other player
    if turn == "w" and turn1 == "WHITE":
        return "b","BLACK"
    else:
        return "w","WHITE"
    

def resultMove(board, action):
    #pawn promotion
    if board[int(action[1])-1][getIntIndex(action[0])] == "wP" and int(action[4])-1 == 7:
        board[int(action[1])-1][getIntIndex(action[0])] = "wQ" #maybe implement selection after with input options and error checking
    if board[int(action[1])-1][getIntIndex(action[0])] == "bP" and int(action[4])-1 == 0:
        board[int(action[1])-1][getIntIndex(action[0])] = "bQ" #maybe implement selection after with input options and error checking

    #piece movement/captures
    # move piece from source location to destination
    board[int(action[4])-1][getIntIndex(action[3])] = board[int(action[1])-1][getIntIndex(action[0])]
    board[int(action[1])-1][getIntIndex(action[0])] = "."
    

def playerInCheck(board, player):
    # returns true if player is in check 
    # player = b or w
    # for each of the player's moves check if opponent king gets captured if it were opponent's turn

    moves = actions(board)
    for move in moves:
        x = getIntIndex(move[0])
        y = int(move[1])-1
        x2 = getIntIndex(move[3])
        y2 = int(move[4])-1
        if board[y][x][0] == getOppositePlayer(player):
            if board[y2][x2] == player+"K":
                return True
    return False

def getOppositePlayer(player):
    if player == "b":
        return "w"
    if player == "w":
        return "b"

def removeIllegalMoves(board, moves):
    # For every possible move, we have to do the move temporarily, check whether the king is in check, and undo the move again. 
    # When the king would be in check, the move is illegal and it is removed. 
    board2 = copy.deepcopy(board)

    # remove any moves that would put player in check
    for move in moves:
        board2 = copy.deepcopy(board) 
        #apply move to board
        resultMove(board2, move)
        #get the player who just made move
        x = getIntIndex(move[0])
        y = int(move[1])-1
        if playerInCheck(board2, board[y][x][0]) == True: 
            moves.remove(move)

    copyMoves = copy.deepcopy(moves)
    #if player currently in check remove moves that dont get rid of check
    if playerInCheck(board, "w") == True:
        for move in moves:
            if board[int(move[1])-1][getIntIndex(move[0])][0] == "w":
                board3 = copy.deepcopy(board)
                resultMove(board3, move)
                if playerInCheck(board3, "w") == True:
                    copyMoves.remove(move)

    #if player currently in check remove moves that dont get rid of check
    if playerInCheck(board, "b") == True:
        for move in moves:
            if board[int(move[1])-1][getIntIndex(move[0])][0] == "b":
                board3 = copy.deepcopy(board)
                resultMove(board3, move)
                if playerInCheck(board3, "b") == True:
                    copyMoves.remove(move)
    return copyMoves

def terminalTest(legalMove, board, player):
    #Check the terminal status of the game. Return true if the game has ended, false otherwise
    playersMoves = []
    for move in legalMove:
        x = getIntIndex(move[0])
        y = int(move[1])-1
        if board[y][x][0] == player:
            playersMoves.append(move)

    ##If there are no legal moves and the king is in check, it’s checkmate for the other color. 
    #       If there are no legal moves and the king is not in check, it’s a stalemate or a draw
    if len(playersMoves) == 0 and playerInCheck(board, player): #Checkmate
        print("Checkmate!")
        return True 
    elif len(playersMoves) == 0: #stalemate
        print("Stalemate!")
        return True
    else:
        return False

def playersMoves(moves, board, player):
    # get all the legals moves for specified player
    playersMoves = []

    for move in moves:
        if board[int(move[1])-1][getIntIndex(move[0])][0] == player:
            playersMoves.append(move)
    return playersMoves

def evalFunction(board, player):
    #Defines an estimate of the expected utility numeric value from a given state for a player
    #score of player - opposite players score
    whiteScore = 0
    blackScore = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]== "wP":
                whiteScore+=10
            if board[i][j]== "wB" or board[i][j]== "wN":
                whiteScore+=30
            if board[i][j]== "wR":
                whiteScore+=50
            if board[i][j]== "wQ":
                whiteScore+=90
            if board[i][j]== "wK":
                whiteScore+=900
            if board[i][j]== "bP":
                blackScore+=10
            if board[i][j]== "bB" or board[i][j]== "bN":
                blackScore+=30
            if board[i][j]== "bR":
                blackScore+=50
            if board[i][j]== "bQ":
                blackScore+=90
            if board[i][j]== "bK":
                blackScore+=900

    if player == "w":
        return whiteScore - blackScore
    else:
        return blackScore - whiteScore

def minimax(board, depth, player, alpha, beta):
    #player = b or w
    legalMoves = removeIllegalMoves(board, actions(board))
    legalMoves2 = playersMoves(legalMoves, board, player)

    if terminalTest(legalMoves2, board, player) == True or depth == 0:
        return "", evalFunction(board, player)
    maxMove = random.choice(legalMoves2)
    moves = legalMoves2

    if player == "w":
        maxEvaluation = -1000000
        for move in moves:
            board2 = copy.deepcopy(board)
            resultMove(board2, move)
            evaluation = minimax(board2, depth-1, getOppositePlayer(player), alpha, beta)[1]

            if (evaluation > maxEvaluation):
                maxEvaluation = evaluation
                bestMove = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            return bestMove, maxEvaluation
    elif player == "b":
        minEvaluation = 1000000
        for move in moves:
            board2 = copy.deepcopy(board)
            resultMove(board2, move)
            evaluation = minimax(board2, depth-1, getOppositePlayer(player), alpha, beta)[1]
            if (evaluation < minEvaluation):
                minEvaluation = evaluation
                bestMove = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            return bestMove, minEvaluation

def drawBoard(boardArray):
    #takes 2d matrix of the board and returns printed board with letters and numbers appended
    board1 = copy.deepcopy(boardArray)
    int = 1
    for x in range(len(board1)):
        board1[x] = [str(int)]+board1[x]
        int+=1
    board1.append([" ", "A", "B", "C", "D", "E", "F", "G", "H"])

    print()
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            print('{:4}'.format(board1[i][j]),end=" ")
        print()
    print()
    return

def main():
    os.system('clear')
    val = input("\nWelcome to the game of chess!\nDo you wish to play 1 player (enter 1) or 2 players (enter 2): ")
    
    #initialize board
    board = [["."]*8 for i in range(8)] 
    board[0] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    board[7] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    board[1] = ["wP" for i in range(8)] 
    board[6] = ["bP" for i in range(8)] 

    #testing
    # board[2][1] = "wQ"
    # board[3][7] = "bB"
    # board[0][0] = "."
    # board[1][5] = "."
    # board[1][6] = "."
    #board[2][5] = "bN"

    #initialize turn
    turn = "w"
    turn1 = "WHITE"
    message = "" 
    alpha = -1000000
    beta = 1000000

    if val == "2": #logic for chess game with 2 players
        moves = removeIllegalMoves(board, actions(board))
        while 1:
            if terminalTest(moves, board, turn) == True:
                break
            os.system('clear')
            drawBoard(board)
            print(turn1 + " TO PLAY")
            print(message)
            moves = [] 
            moves = removeIllegalMoves(board, actions(board))
            print("Possible moves:")
            print(playersMoves(moves, board, turn))
            
            input1 = input("input: ")
            #checks piece is the right colour and user enters valid move: 
            if input1 in moves and board[int(input1[1])-1][getIntIndex(input1[0])][0] == turn:
                resultMove(board, input1)
                turn, turn1 = switchTurn(turn, turn1)

        turn, turn1 = switchTurn(turn, turn1) #switch back to winner cause game exits loop on losers turn
        print("Game Over "+ turn1+ " won the game")

    if val == "1":
        val2 = input("\nWould you like to play white (enter w) or black (enter b): ")
        if val2 == "b":
            moves = removeIllegalMoves(board,actions(board))
            while 1:
                if terminalTest(moves, board, turn) == True:
                    break
                os.system('clear')
                drawBoard(board)
                print(turn1 + " TO PLAY")
                print(message)
                moves = [] 
                moves = removeIllegalMoves(board, actions(board))
                print("Possible moves:")
                print(playersMoves(moves, board, turn))
                
                if turn == "b":
                    input1 = input("input: ")
                    #checks piece is the right colour and user enters valid move: 
                    if input1 in moves and board[int(input1[1])-1][getIntIndex(input1[0])][0] == turn:
                        resultMove(board, input1)
                        turn, turn1 = switchTurn(turn, turn1)
                else:
                    resultMove(board, minimax(board, 5, turn, alpha, beta)[0])
                    turn, turn1 = switchTurn(turn, turn1)
            turn, turn1 = switchTurn(turn, turn1) #switch back to winner cause game exits loop on losers turn
            print("Game Over "+ turn1+ " won the game")

        if val2 == "w":
            moves = removeIllegalMoves(board,actions(board))
            while 1:
                if terminalTest(moves, board, turn) == True:
                    break
                os.system('clear')
                drawBoard(board)
                print(turn1 + " TO PLAY")
                print(message)
                moves = [] 
                moves = removeIllegalMoves(board, actions(board))
                print("Possible moves:")
                print(playersMoves(moves, board, turn))
                
                if turn == "w":
                    input1 = input("input: ")
                    #checks piece is the right colour and user enters valid move: 
                    if input1 in moves and board[int(input1[1])-1][getIntIndex(input1[0])][0] == turn:
                        resultMove(board, input1)
                        turn, turn1 = switchTurn(turn, turn1)
                else:
                    resultMove(board, minimax(board, 5, turn, alpha, beta)[0])
                    turn, turn1 = switchTurn(turn, turn1)
            turn, turn1 = switchTurn(turn, turn1) #switch back to winner cause game exits loop on losers turn
            print("Game Over "+ turn1+ " won the game")
main()
