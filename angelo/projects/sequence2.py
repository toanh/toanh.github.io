graphics.clear(0, 0, 0)

# moving text up
y = 0
while y < 100:
    graphics.clear(0, 0, 0)
    graphics.drawText("Hello!", 200, y, fontSize = 30)
    y = y + 2

# bit of a pause
graphics.sleep(1000)

# moving text down
while y > 0:
    graphics.clear(0, 0, 0)
    graphics.drawText("Hello!", 200, y, fontSize = 30)
    y = y - 2

# waiting for A key press
x = 110
y = 200
while True:
    if graphics.isKeyPressed(KEY_A):
        x = x - 2
    if graphics.isKeyPressed(KEY_D):
        x = x + 2
    if graphics.isKeyPressed(KEY_S):
        break
    graphics.clear(0, 0, 0)
    graphics.drawText("Press S to start", x, y, fontSize = 30, r = 1, g = 0, b = 0)
    
# win game screen (or new level etc.)
graphics.clear(0, 0, 1)
graphics.drawText("You won!!!", 150, 200, fontSize = 30)
    
    