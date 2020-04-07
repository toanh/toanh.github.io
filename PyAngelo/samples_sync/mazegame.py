pyangelo = TextSprite("😀", x = 0, y = 0, fontSize = 20, fontName = "Arial")
goal = TextSprite("🧦", x = 470, y = 370, fontSize = 20, fontName = "Arial")

win = False

@loop_animation
# saving old position
oldx = pyangelo.x
oldy = pyangelo.y

# checking for keys
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    pyangelo.x = pyangelo.x - 1
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    pyangelo.x = pyangelo.x + 1
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    pyangelo.y = pyangelo.y + 1
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    pyangelo.y = pyangelo.y - 1
    
# clears the screen to black
graphics.clear(0.7, 0.7, 0.7, 1.0)
# draw the level from a user-created and uploaded image
graphics.drawImage("https://i.imgur.com/ACAWSsV.png", 0, 0)
    
colour = graphics.getPixelColour(pyangelo.x + pyangelo.width/2, pyangelo.y + pyangelo.height/2)
# if pixel is dark grey -> black, block path
if colour.r < 0.2 and colour.g < 0.2 and colour.b < 0.2:
    pyangelo.x = oldx
    pyangelo.y = oldy
    
if pyangelo.overlaps(goal):
    win = True

graphics.drawSprite(goal)
graphics.drawSprite(pyangelo)
if win == True:
    # shadow effect
    graphics.drawText(f"You won!!!", 157, 157, fontSize = 28, r = 1, g = 0, b = 0)
    graphics.drawText(f"You won!!!", 160, 160, fontSize = 28, r = 1, g = 1, b = 1)