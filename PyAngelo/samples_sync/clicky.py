from random import *

pyangelo = Sprite("https://pyangelo.github.io/PyAngelo.png", 0, 0)

# loop forever
@graphics.loop
def Game():
    mousePos = graphics.getMousePos()
    
    if pyangelo.contains(mousePos):
        pyangelo.x = randint(0, graphics.width - pyangelo.image.width) 
        pyangelo.y = randint(0, graphics.height - pyangelo.image.height) 
        
    # clears the screen to black
    graphics.clear(0.0, 0.0, 0.0, 1.0)

    # draws the image at the updated x and y coordinates
    graphics.drawSprite(pyangelo)
    
    graphics.drawText("Don't click PyAngelo!", 125, 0, fontSize = 20)