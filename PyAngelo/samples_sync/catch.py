# for picking random numbers
from random import *

# setting up the text sprites
ball1 = TextSprite("🏀 ", x = 195, y = 400)
ball2 = TextSprite("🏀 ", x = 300, y = 400)
catcher = TextSprite("✋ 🤚", x = 195, y = 10)

score = 0
# the playing variable lets the loop_animation decide whether to play
# the game or show the game over screen
playing= True

# play music at lower volume and looped
graphics.playSound("sounds/Lemmings_01.mp3", volume = 0.1, loop = True)

@loop_animation

# make the balls fall down at different speeds
ball1.y = ball1.y - 1
ball2.y = ball2.y - 2

# player controls
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    catcher.x = catcher.x - 1
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    catcher.x = catcher.x + 1

# has the player caught the ball(s)?
if catcher.overlaps(ball1):
    # add to score
    score=score+1
    # move ball back up to the top
    ball1.y = 400
    # start at a new random x position
    ball1.x = randint (0, 370)
# same logic for the 2nd ball
if catcher.overlaps(ball2):
    score=score+1
    ball2.y = 400
    ball2.x = randint (0, 370)

# check if the balls have fallen off the screen, if so, change the
# playing variable to False (so that the end-game screen will be shown later)
if ball1.y <= 0 or ball2.y <= 0:
    playing = False
    
# depending the value of the playing variable: we either play the game,
# or display the end-game screen
if playing == True:
    graphics.clear(0, 0, 0)
    graphics.drawSprite(ball1)
    graphics.drawSprite(ball2)
    graphics.drawSprite(catcher)
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
else:
    graphics.clear()
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)