
# AESTHETICS

WHAT WENT WELL
* I am very happy with the aesthetic appearance of my game:
    * The snooker table is is accurately proportioned; I researched this before implementing the design
    * The information displayed within the game window is clear
    * Movement of sprites is smooth
    * The cue implementation does not require too much thought and looks accurate
    * The game is colorful and appealing

POTENTIAL IMPROVEMENTS
* In order to make my game look more shelf ready:
    * I would explore the possibility of drawing the circular balls to higher precision so they look more realistic; they are currently slightly pixellated
    * I would improve the text outputs to make them more aesthetically pleasing

# FUNCTION

WHAT WENT WELL
* The game functions as I inteded it to for the most part:
    * The ball collisions are highly accurate (with pockets, other balls and rails)
    * I am particularly proud of my implementation of the foul function for potting the white and the resulting ball in hand 
    * The guide cue line provides a good aid to the player whilst not reducing the difficulty of the game too much
    * The general rules of real-world snooker are all present within the game so would be accurate and appealing for the target audience
    * The scoring system and the highscore system provide a challenge and goal for the player which will keep them engaged
    * There are no unexpected logical errors whilst playing all parts of the game
    * The option ro re-play, whilst simple, is a good addition

POTENTIAL IMPROVEMENTS
* Most of the improvements regard implementing the more niche rules of the game:
    * A future development would include conditions for fouls in certain circumstances (e.g. potting the pink after hitting blue first)
    * The table I find does not have enough room at the top and left hand side to play a shot with high power, however this would be difficult to change as many of the sprites' positions are dependent on the window size
    * A better tiebreaker would be to respot the black ball; this would be more satisfying for the user with no ties, especially since games take a long time
    * A final version could contain additional guidance, my implementation may require looking over the README file for some players who havent played snooker
    * I could include a message system for fouls so players can track the game better

# CODING STYLE AND CONSTRUCTION

WHAT WENT WELL
* The most important part of the game is its object orientated setup
* Class inheritence from ball &rarr; moving ball, as well as movingball &rarr; Cueball is sound implementation
* The solution is well procedurised, with certain routines such as the file writing and the construction algorithms for the balls and table within their own functions which improves readability
* The solution is highly modular so objects and subroutines could be used for similar games (such as 8 ball pool)
* I explored new constructs such as error handling to deal with removing sprites whilst continuing the gameloop
* This is the first game I have created that can save data permenantly to text files (High scores)
* My methods are, I believe, highly efficient
* I have created procedures that can be re-used by multiple instances of objects and have little redundent code

POTENTIAL IMPROVEMENTS
* There may be some redundency where operations are carried out twice; I could remove this by parsing through my code, taking pieces out and re-testing
* I could decompose my procedures further to try and eliminate any repeated code within functions
* I could better procedurise the main gameloop to make my code more readable
* I maybe could have used finite states to split up behaviours of the cueball for normal play/ ball in hand etc.

# SUMMARY

**If I were to start this project again** I could re-use many of the objects and functions/subroutines, however I would focus on the aesthetic design and centering the table. I would also make the playing surface bigger or resizable with the window. I would also like to include some more of the foul rules of snooker as my current game is not completely representitve of an actual snooker game.

**If I were to continue with this project** I would potentially create a pool game mode using the subroutines that apply since most of the game physics are the same. I would also improve the aesthetic of the labels that display scoring information as well as creating full screen text alerts in case of fouls or when important information needs to be relayed to the player. A large addition to the game would be to add the repotted black tie-breaker; whilst this would be possible by copying pieces of code into a new tiebreaker game loop, this may be better implemented by procedurising my main code then using the snippets that apply.

# WHAT I HAVE LEARNED

* Built-in sort using a lambda function
* How to recognise different keys being pressed within the gameloop and how to give those actions behaviours
* Exception handling in python
* How to use multiple gameloops with different purposes to create a timetline to the game
* Trigonometric math to draw the pool cue/ guide line
* Reading/writing from text files
* Friction game physics to reduce velocities

Note: I did not work as a group so all work on Snooker Game is my own and was completed within the bounds of the Honor Code