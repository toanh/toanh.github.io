from random import *

# set up basket position
basket_x = 0
basket_y = 10

# egg
egg_x = randint(0, 490)
egg_y = 400

score = 0

# loop forever
@graphics.loop
def Game():
    global basket_x, basket_y, egg_x, egg_y, score
    
    # if the 'A' is pressed update the x coordinate to move 1 pixel left
    if graphics.isKeyPressed(KEY_A):
        basket_x = basket_x - 1
        
    # if the 'D' is pressed update the x coordinate to move 1 pixel right
    if graphics.isKeyPressed(KEY_D):
        basket_x = basket_x + 1
        
    egg_y -= 1
    
    if egg_y < 0:
        egg_x = randint(0, 490)
        egg_y = 400
        
    if graphics.overlaps(basket_x, basket_y, 50, 10, egg_x, egg_y, 12, 12):
        score += 1
        egg_x = randint(0, 490)
        egg_y = 400
        
    # clears the screen to black
    graphics.clear(0.0, 0.0, 0.0, 1.0)
    
    graphics.drawText("Score: " + str(score), 0, 0)
    
    graphics.drawCircle(egg_x, egg_y, 6, 1, 1, 1)
    # draws the image at the updated x and y coordinates
    graphics.drawRect(basket_x, basket_y, 50, 10, 0, 1, 0)
