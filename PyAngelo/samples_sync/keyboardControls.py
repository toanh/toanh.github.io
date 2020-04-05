pyangelo = Sprite("https://pyangelo.github.io/PyAngelo.png", 0, 0)

# loop forever
@loop_animation
# if the 'A' is pressed update the x coordinate to move 1 pixel left
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    pyangelo.x = pyangelo.x - 1
    
# if the 'D' is pressed update the x coordinate to move 1 pixel right
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    pyangelo.x = pyangelo.x + 1
    
# if the 'W' is pressed update the x coordinate to move 1 pixel up
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    pyangelo.y = pyangelo.y + 1
    
# if the 'S' is pressed update the x coordinate to move 1 pixel down
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    pyangelo.y = pyangelo.y - 1
    
# clears the screen to black
graphics.clear(0.0, 0.0, 0.0, 1.0)

# Writing the instructions
graphics.drawText("Use the W,A,S,D keys to move PyAngelo!", 100, 200, fontSize = 12)

# draws the image at the updated x and y coordinates
graphics.drawSprite(pyangelo)