# OUTLINE

* My final project will be a table based game - originally I thought pool would be a good option however there are many examples of pool games currently available and therefore it is unlikely I would be able to produce anything novel or approaching the complexity of what is currently on the market.

* Since pool games already exist i will use '8 ball pool' as well as real-world billiard tables for reference when designing and implementing my game.

* An alternative to pool that will allow me to display additional conditional constraints as well as game physics including vector math and forces such as friction would be snooker. Snooker has many niche rules that differ from pool and there are not many options currently available therefore my game would be attractive to potential users. I have the added advantage that I play snooker and therefore know the rules well; I also would be highly interested in having a virtual copy of the game and am excited to see if I can replicate it in a professional manner.

* I hope to make a snooker game with rules as follows:
    1. The game is played by 2 players
    2. There are different colored balls &rarr; red, yellow, green, brown, blue, pink black
    3. The balls have different values &rarr; 1, 2, 3, 4, 5, 6 and 7 respectively
    4. The player controls a cue ball which they can stike at varying velocities and at whatever angle/direction they wish
    5. All balls must remain on the surface of the table unless they are potted
    6. Potted red balls are removed from the table
    7. Potted colored balls are removed initially then returned to the table after the balls have stopped moving
    8. Once there are no red balls left on the table, colored balls should not be added back to the table after they are potted
    9. The colored balls should be potted in order yellow, green, brown, blue, pink, black when there are no reds on the table

    * Foul Rules
        1. If the white ball is potted a foul is recorded and the other player is given 4 points
        2. If a color is potted at the same time as a red the opposing player will be awarded the value of the color or 4 points (whichever is higher)
        3. Once the white ball is potted the other player has ball in hand so is able to move the cue ball to wherever they wish on the table
        
    If the user fails to pot a ball the next user is given a turn and so on therefore it can be said the users take alternate turns like in pool
    A player wins by having the most points when there are no balls left on the table

# ADDITIONAL FEATURES / THE FUTURE

* Additionally, in snooker a break is described as the value of the balls potted in one trip to the table i.e. one 'go.' I will aim to have some tracking mechanism that records a user's highest break or a leaderboard of high breaks to male the game more competitive rather than just being a 1v1 thing.

* I would also like to include a single player mode with different ball set-ups. In real world snooker there are many training methods that could be emulated to make players better att the game in a training section. This may not be possible due to time constraints of the release however and I would therefore aim to include this in a later version.

* Inside a wider relese, leaderboards would be local or global so the user could compare themself with other players. Incentives like in-game currency could also be offered in order to buy table skins etc or trophies could be an interesting way of keeping players engaged in a fun, competitive environment

# WHY?

* I believe this game will ultimately prove to be successful as games like the aforementioned '8 ball pool' have proved people find 1v1 games interesting and fun to play

* I also believe this game shows well how the game pysics taught in class can be applied to real-world sports/games to recreate them on a digital medium. Momentum conserving collisions, friction and the normal contact force from the cue are all fairly routine to translate into python whilst the conditional aspects of the game rules will be tough. 

* Options currently offered are not well advertised or don't have the star power to draw users and I hope my implementation would be different

# UPSHOT

I hope to be able to implement all the features as above. If I am unable to do so I will ammend my readme to make the rules of my version of the game clear. Some features will not be possible in the required timeframe or would be better implemented in other languages or with other APIs. I will be working alone on the project so all work is my own. I hope you and others enjoy playing my game :)

