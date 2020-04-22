from math import *

# creating a list of TextSprites
sprites = []
sprites.append(TextSprite("😷", x = 0, y = 400))
sprites.append(TextSprite("🤯", x = 50, y = 400))
sprites.append(TextSprite("🤑", x = 100, y = 400))
sprites.append(TextSprite("😽", x = 150, y = 400))
sprites.append(TextSprite("😎", x = 200, y = 400))
sprites.append(TextSprite("👨", x = 250, y = 400))
sprites.append(TextSprite("👩", x = 300, y = 400))
sprites.append(TextSprite("🧛", x = 350, y = 400))
sprites.append(TextSprite("💋", x = 400, y = 400))
sprites.append(TextSprite("👔", x = 450, y = 400))

# start time at 0
t = 0

@loop_animation
# move forward in time
t += 0.05

# position the sprites on a sinusoidal wave
for pyangelo in sprites:
    # the offset in the sine wave is based on the x position
    offset = pyangelo.x / 500 * 3.14159
    pyangelo.y = 200 + 150 * sin(t + offset)
    # the derivative is the direction
    pyangelo.dy = -cos(t + offset)

# clears the screen to black
graphics.clear(0, 0, 0)

# draws the sprites at their coordinates
for pyangelo in sprites:
    # sprites moving down are drawn behind (before) the text
    if pyangelo.dy > 0:
        graphics.drawSprite(pyangelo)
    
# display the text
graphics.drawText("Hello, world!", x = 100, y = 170, fontSize = 40, r = 1, g = 1, b = 1)

# draws the sprites at their coordinates
for pyangelo in sprites:
    # sprites moving up are drawn in front of (after) the text
    if pyangelo.dy < 0:
        graphics.drawSprite(pyangelo)