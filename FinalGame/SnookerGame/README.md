---------------------- Snooker Game ----------------------

* The objective of the game is to pot balls in order red -> color and repeat
* Ball values are as follows:
    * Red &rarr; 1
    * Yellow &rarr; 2
    * Green &rarr; 3
    * Brown &rarr; 4
    * Blue &rarr; 5
    * Pink &rarr; 6
    * Black &rarr; 7

------- Fouls -------

* Fouls are recorded if the cueball is potted and the oponent is given 4 points as a result
* Fouls are also recorded if more than one ball with a different value is potted in one turn

* When the cueball is potted the player has 'ball in hand' and so the cue does not appear after the white is respotted
* The user must click on a point on the table for the cueball to be placed for their next shot

------- General -------

* If the player misses a shot or fouls, it becomes the next player's turn
* The current player is displayed on the screen to prevent any confusion
* The player's 'break' is the total of the balls they have potted in one turn at the table and this is displayed on screen
* There is a high break leaderboard which is held in a text file and therefore the player;s break may be saved if they record a new record break

* When a color is potted, it is re-added to the table in its original position
* When a red is potted it is not re-added to the table
* Once all the reds have been potted the colors are no longer re-added to the table when they are potted respectively

------- Win Condition -------

* A player wins by obtaining a higher score than their oponent once all balls on the table are potted
* If the players'scores are equal, the black is respotted and the first person to pot the black wins
* If a player fouls on the black respot they automatically lose

