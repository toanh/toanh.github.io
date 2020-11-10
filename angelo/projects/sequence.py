graphics.clear(0, 0, 0)
graphics.drawText("👇Look below", 0, 130, fontSize = 30)

graphics.sleep(1000)

# moving text in
x = -110
while x < 100:
    graphics.clear(0, 0, 0)
    graphics.drawText("Hello!", x, 100, fontSize = 30)
    x = x + 2

# bit of a pause
graphics.sleep(1000)

# moving text out
while x > -110:
    graphics.clear(0, 0, 0)
    graphics.drawText("Hello!", x, 100, fontSize = 30)
    x = x - 2

# waiting for A key press
while graphics.isKeyPressed(KEY_A) == False:
    graphics.clear(0, 0, 0)
    graphics.drawText("Press A to start", 110, 200, fontSize = 30, r = 1, g = 0, b = 0)

# start our game!
r = 0
x = 100
y = 100
direction = 0.01
while True:
    graphics.clear(r, 0, 0)
    r = r + direction
    if r >= 1.0:
        direction = -0.01
    elif r <= 0.0:
        direction = 0.01
    graphics.drawText("👶", x, y, fontSize = 30)
    if graphics.isKeyPressed(KEY_A):
        x = x - 1
    if graphics.isKeyPressed(KEY_D):
        x = x + 1
    if graphics.isKeyPressed(KEY_W):
        y = y + 1
    if graphics.isKeyPressed(KEY_S):
        y = y - 1
    if x < 0:
        # if hits edge, display some text for 1 sec pause
        graphics.drawText("You can't touch the edge!",0, 300, fontSize = 30)
        graphics.sleep(1000)
        x = 0
    # pressing Q to quit
    if graphics.isKeyPressed(KEY_Q):
        break
    
# end game screen (or new level etc.)
graphics.clear(0, 1, 0)
graphics.drawText("Game Over!!!", 0, 0, fontSize = 30)
    
    