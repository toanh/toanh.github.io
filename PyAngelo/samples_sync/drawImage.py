pyangelo = Sprite("https://pyangelo.github.io/PyAngelo.png", 0, 100)

@graphics.loop
def Game():
    # clears the screen to black
    graphics.clear(0, 0, 0)
    
    # draws the sprite at coordinates (x = 0, y = 100)
    graphics.drawSprite(pyangelo)