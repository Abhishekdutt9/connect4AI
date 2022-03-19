# connect4AI
This is an artificial intelligence bot that plays an extended version of the connect four game. You can start playing the game using the command line arguments initializing the size of the board, the type of algorithm.
The bot uses minimax algorithm along with alpha beta pruning to select the best moves. 

# How to start playing the game
Step 1: Pull the repo <br>
Step 2: $ python connect383.py h c 6 7 --depth 3<br>
        Enter the line above to play the game where the human (h) moves first and the computer (c) moves second, this can be switched if you want to move second. 6 and 7 represent the size of the board, this can be changed to any whole number, but be aware, computational time would increase exponentially. depth 3 is nothing but how far ahead the AI will see before making a judgement, lower levels of depth like 1, would result in bad decisions, higher levels of depth would result in slower computation, depths of 3/4 are ideal<br>
Step 4: Once you run Step 2, a board will show up in the terminal window, you can select the number of the column where you would like to place your token.<br> 
Step 5: A score would be shown on the terminal, a positive score means that player 1 is in the lead, a negative score means that player 2 is in the lead.<br>
step 6: The game will end once the board is full. Good Luck!! <br>
