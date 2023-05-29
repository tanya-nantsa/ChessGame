# ChessGame

## How To Run Game
To run the game ensure you are in the project directory and enter 'python3 chess.py'.

## How To Play
Select whether you want play the two player or one player version of the game by entering either '1' or '2'.
If user selects 1 player version they must specify which colour they wish to play as by entering either
'b' or 'w'.

Each chess piece is represented by two characters. The first character is either b and w, signifying which 
pieces belong to black and white. The second character represents which type of chess piece it is. 
P = Pawn, R = Rook, N = Knight, B = Bishop, Q = Queen, and K = King.b

White will always play first. To play a move enter the staring position of the piece you would like to 
move along with the the destination location of that piece. For example to move a piece located at C7 on
the board to the location C5 on the board the user must enter 'C7 C5'. All available maves the player can make 
are listed under the board. If a player makes an illegal move the same player will have to play again.

## Details About The Game's Design
In this game I have created a basic chess AI for the 1 player version. To create the AI I implemented 
a min-max tree with A-B pruning.

Evaluation function:
Every piece on the board was given a value. The score was calculated by getting the total value of all the 
pieces for each player on the board and then finding the difference in score between players.