# ChessGame

## How To Run Game
To run the game ensure you are in the project directory and enter 'python3 chess.py'.

## How To Play
Select whether you want play the two player or one player version of the game by entering either '1' or '2'.
If user selects 1 player version they must specify which colour they wish to play as by entering either
'b' or 'w'.

Each chess piece is represented by two characters. The first character is either b and w, signifying which 
pieces belong to black and white. The second character represents which type of chess piece it is. 
P = Pawn, R = Rook, N = Knight, B = Bishop, Q = Queen, and K = King.

White will always play first. To play a move enter the starting position of the piece you would like to 
move along with the destination location of that piece. For example to move a piece located at C7 on
the board to the location C5 on the board the user must enter 'C7 C5'. All available moves the player can make 
are listed under the board. If a player makes an illegal move that player will have to play again.

The game is over when there is a checkmate or a stalemate (no legal moves).

## Details About The Game's Design
In this game I have created a basic chess AI for the 1 player version. To create the AI I implemented 
a min-max tree with A-B pruning.

Evaluation function:
Every piece on the board was given a value. The values are as follows: Pawn = 10, Bishop = 30,
Rook = 50, Queen = 90, and King = 100. The score was calculated by getting the total value of 
all the pieces for each player on the board and then finding the difference in score between players.
The evaulation function is used to calculate the best moves within the min-max tree.

<img width="590" alt="Screen Shot 2023-05-29 at 3 07 01 PM" src="https://github.com/tanya-nantsa/ChessGame/assets/77226151/7fc9c538-83ac-4c3c-bfea-13968cb5a68b">

<img width="590" alt="Screen Shot 2023-05-29 at 3 07 15 PM" src="https://github.com/tanya-nantsa/ChessGame/assets/77226151/aa4d176b-c1c2-453e-8114-0363469d19b3">

<img width="590" alt="Screen Shot 2023-05-29 at 3 07 37 PM" src="https://github.com/tanya-nantsa/ChessGame/assets/77226151/47aeb9e5-75cc-4642-99be-0b392f69aa4d">
