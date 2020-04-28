imageURL = "https://pyangelo.github.io/PyAngelo.png"

# the sprite will be using the image from the URL above
# and it's starting (x, y) coordinates will be (195, 400)
pyangelo = Sprite(imageURL, x = 195, y = 400, width = 250, height = 100)

# whether pyangelo is growing or shrinking
dirHeight = 1
dirWidth = 0

@loop_animation

# move the sprite down a little
pyangelo.width = pyangelo.getWidth() + dirWidth
pyangelo.height = pyangelo.getHeight() + dirHeight

if pyangelo.getHeight() > 200:
    pyangelo.height = 200
    dirHeight = -dirHeight
elif pyangelo.getHeight() < 96:
    pyangelo.height = 96
    dirHeight = 0
    dirWidth = 1
if pyangelo.getWidth() > 300:
    pyangelo.width = 300
    dirWidth = -dirWidth
elif pyangelo.getWidth() < 200:
    pyangelo.width = 200
    dirWidth = 0
    dirHeight = 1

# centre pyangelo on the screen
pyangelo.x = (graphics.width - pyangelo.getWidth()) / 2
pyangelo.y = (graphics.height - pyangelo.getHeight()) / 2

# clears the screen to black
graphics.clear(0, 0, 0)

# draws the sprite at its coordinates
graphics.drawSprite(pyangelo)