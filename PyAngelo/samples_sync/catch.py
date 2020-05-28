from random import *
ball = TextSprite("🏀 ", x = 195, y = 400)
catcher = TextSprite("✋ 🤚", x = 195, y = 10)

score = 0
playing= True

@loop_animation

ball.y = ball.y - 1


if ball.y < 0:
    ball.y = 400

if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    catcher.x = catcher.x - 1
    
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    catcher.x = catcher.x + 1

if catcher.overlaps(ball):
    score=score+1
    ball.y = 400
    ball.x = randint (0, 370)

if ball.y <=0:
    playing = False
    

if playing == True:
    graphics.clear(0, 0, 0)
    graphics.drawSprite(ball)
    graphics.drawSprite(catcher)
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
else:
    graphics.clear()
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)