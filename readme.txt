Names-
Abhishek Dutt
Shruti Shelke

Name of bot- something sus

So the whole idea behind the bot is that it not only uses the score() function, but it also checks for all the places that are empty where a next move could be played. We include the empty place into our streaks function too and calculate the score based of that. We also have an alpha that increases with the move played in the middle of the board and is less when the move is played in the side, allowing the bot to make more central moves however we made sure that this alpha does not overpower the actual score and evaluation methods so that the bot also plays in the sides when it feels that is the sole best move. But, when there are two best moves, the both will choose the move which places the token closer to the center of the board as this increases the chances of winning.
I think it is a pretty effective algorithm. I tested it by playing against it and making a few friends and family play against it too, I was extremely happy with the bot. 

The test_boards.py has a couple of test boards, a few of them which were already provided, one of the board is similar to the board Prof. Matthew spoke about in class, during discussion 11. This is the board named your_test, I use this board to make sure that my algorithm does not choose the score() greedy approach, as the score function with a depth of 2 takes us to an outcome that is not the best in the end. The other tests are just used to see if the algorithm is smart enough to make the best moves. All these tests pass successfully.

Everything in the code is working. 
