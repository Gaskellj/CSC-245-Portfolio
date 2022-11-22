11/18/2022

1. Created the frame of the snooker table with rounded edges
2. Created the inside playing surface of the pool table
3. Created the rails for the snooker balls to collide with using a new Rail class
4. Created the six pockets using Pocket class
5. Added the cueball as the first moving ball
6. Created the cue class to draw the cue and represent the power with which the ball will be struck
7. Added the guide vector line to the cue so the player can see where the ball is going
8. Added the function that makes the cue longer/shorter depending on the shot power
9. Introduced friction (more realistic with the square multiplier to better mimic real world pysics)
10. Rolled the friction into the simulate function so whenever velocity > 0; friction will occur on all balls

11/19/2022

11. Created the baulk line and the semi circle
12. Used the cue Vector to make a resultant vector for the ball to travel on
13. Created a button click down condition to record a shot being taken
14. Created the instruction for the cueball to move along the resultant vector with a force applied consistent with the cue length
15. Added aditional friction coefficient of 0.92 to the rails to better mimic real world physics since the rails remove some momentum
16. Created the rest of the balls and initialised their positions on the table
17. Added a value attribute for each ball 
18. Added collision physics for cueball with other balls
19. Added collision physics for object ball with object ball
20. Added a friction coefficient to reduce the momentum of both balls after a collision
21. Added ball-pocket collisions
22. Added a remove function to remove balls that have been potted

11/20/2022

23. Created a respot list for colored balls that need respotting after being potted
24. Created a loop to parse through the respot list after all balls are stationary and add them to the balls list again at their original position
25. Created Player1 and Player2 variables to track names and scores
26. Added the sign in pages for player 1 and 2
27. Added backspace functionality to the sign in pages
29. Added foul behaviour for the cueball
30. Rolled the cueball into the respot loop to prevent it being respotted whilst balls are still moving
31. Fixed a bug by creating a new cueball and deleting the old one every time it is potted
32. Introduced a change in player after the cueball is potted
33. Used exception handling to stop cue_ball being referenced before it is added back to the game
34. Added ball in hand behaviour so if the cueball is potted it can be moved by the next player
35. Added a conditon to trigger a change in player after balls stop moving when a shot has been played
36. Ammended the condition to check if a non-foul pot has been made by the player

11/21/2022

37. Treats a color as a red (except for ball value) when all the reds have been potted i.e. ball count <= 5 as per snooker rules - not respotted
38. Added a text file to track highest breaks
39. Created a function to read the highscores into the game
40. Created a loop to display the highscores on the screen using labels
41. Created a function to return the highscores in order
41. Added a check to see if current break is higher than a highscore in the HighScores list
42. Added functionality to replace the lowest score in HighScores if the current break is higher
43. Created a write function to overwrite the HighBreak text file when a new high score is recorded
44. 



