# Pong-Game
Use the pygame library, which is commonly used for game development in Python. If you haven't already, you'll need to install 'pygame'

Pong is a classic two-player arcade game that simulates a table tennis match. The game's objective is to score points by hitting a ball past your opponent's paddle. 

Game Setup:

The game is played on a rectangular screen divided by a centerline. Two paddles are placed on opposite sides of the screen, and a ball is placed in the center.
The player controls the left side, and the computer opponent controls the right side.

Gameplay:

The player controls their paddle using the up and down arrow keys. The goal is to prevent the ball from passing their paddle and send it towards the opponent's side.
The ball starts moving at a certain speed, and its direction can change upon colliding with the top, bottom, or paddles.
When the ball collides with a paddle, its horizontal direction is reversed, simulating the bouncing effect.

Scoring:

If the ball passes the opponent's paddle and goes off the screen on the left side, the player scores a point.
If the ball passes the player's paddle and goes off the screen on the right side, the opponent scores a point.
The game continues until a certain number of points are scored or until the player chooses to quit.

Game Over:

The game ends when one player reaches the specified score limit or when the player chooses to quit.
The player with the higher score at the end of the game wins.
