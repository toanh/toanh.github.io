from random import *

basket = Sprite(Rectangle(0, 10, 50, 10), r = 0, g = 1, b = 0)

egg = Sprite(Circle(200, 400, 6), r = 0, g = 1, b = 1)

score = 0

# loop forever
@loop_animation    
# if the 'A' is pressed update the x coordinate to move 1 pixel left
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    basket.x = basket.x - 1
    
# if the 'D' is pressed update the x coordinate to move 1 pixel right
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    basket.x = basket.x + 1
    
egg.y -= 1

if egg.y < 0:
    egg.x = randint(0, 490)
    egg.y = 400
    
if basket.overlaps(egg):
    score += 1
    egg.x = randint(0, 490)
    egg.y = 400
    
# clears the screen to black
graphics.clear(0.0, 0.0, 0.0, 1.0)

graphics.drawText("Score: " + str(score), 200, 370, fontSize=20)

graphics.drawSprite(egg)
graphics.drawSprite(basket)
