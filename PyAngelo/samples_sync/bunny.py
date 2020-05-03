# create our sprites
# in this case, our sprites are TextSprites, but you can freely use a mixture
# of image sprites and TextSprites too
bunny = TextSprite("🐰", fontSize = 30, r = 0, g = 1, b = 0)
carrot = TextSprite("🥕", x = 400, y = 150, fontSize = 20, r = 0, g = 1, b = 1)

# loop forever
@loop_animation    

# checking for keys or virtual d-pad presses
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    bunny.x = bunny.x - 1
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    bunny.x = bunny.x + 1
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    bunny.y = bunny.y + 1
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    bunny.y = bunny.y - 1

# does the bunny overlap the carrot?
if bunny.overlaps(carrot):
    # scoot the carrot to the left
    carrot.x -= carrot.getWidth()
    # play the sound effect
    graphics.playSound("sounds/speed.mp3")

# clears the screen to black
graphics.clear(0.0, 0.0, 0.0, 1.0)

# draw our sprites
graphics.drawSprite(carrot)
graphics.drawSprite(bunny)
