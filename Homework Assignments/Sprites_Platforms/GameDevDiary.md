1) Copied and edited the go_right function to go_left, flipped the vector to negative
2) Created the jump method to increase the y velocity and make the sprite move upwards
3) Created the gravity function to reduce the velocity to decelerate the sprite then accelerate in the negative direction
4) Use the transform.flip function to flip the sprite image if x velocity is negative
5) Split the stop functioninto stop_x and stop_y to allow for jump arcs
6) Used stop_x and stop_y to stop the sprite after a collision and move the sprite away from the block
    so the collision is no longer occuring
7) Created the boolean jumping to ensure the sprite cannot double jump