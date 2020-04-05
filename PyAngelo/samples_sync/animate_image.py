imageURL = "https://pyangelo.github.io/PyAngelo.png"

# the sprite will be using the image from the URL above
# and it's starting (x, y) coordinates will be (195, 400)
pyangelo = Sprite(imageURL, x = 195, y = 400)

@loop_animation

# move the sprite down a little
pyangelo.y = pyangelo.y - 1

# has it gone off the bottom?
if pyangelo.y < 0:
    # reset it back to the top
    pyangelo.y = 400

# clears the screen to black
graphics.clear(0, 0, 0)

# draws the sprite at its coordinates
graphics.drawSprite(pyangelo)