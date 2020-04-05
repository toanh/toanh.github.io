imageURL = "https://pyangelo.github.io/PyAngelo.png"

# the sprite will be using the image from the URL above
# and it's starting (x, y) coordinates will be (0, 100)
pyangelo = Sprite(imageURL, x = 0, y = 100)

@loop_animation

# clears the screen to black
graphics.clear(0, 0, 0)

# draws the sprite at the coordinates it was set up with
graphics.drawSprite(pyangelo)