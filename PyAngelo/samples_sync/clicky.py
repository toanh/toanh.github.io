from random import *

pyangelo = Sprite("https://pyangelo.github.io/PyAngelo.png", 0, 0)

@loop_animation
mousePos = graphics.getMousePos()

# check if the mouse/touch coordinates are within the sprite
if pyangelo.contains(mousePos):
    # if so, move the sprite to a new random location
    pyangelo.x = randint(0, 400) 
    pyangelo.y = randint(0, 300) 
    
# clears the screen to black
graphics.clear(0.0, 0.0, 0.0, 1.0)

# draws the image at the updated x and y coordinates
graphics.drawSprite(pyangelo)

graphics.drawText("Don't click PyAngelo!", 125, 0, fontSize = 20)