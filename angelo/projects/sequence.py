graphics.clear(0, 0, 0)
graphics.drawText("👇Look below", 0, 130, fontSize = 30)

# pause
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
# level 1
x = 100
y = 100

while True:
    graphics.clear(1, 0, 0)
    graphics.drawText("👈 Don't go here", 0, 350, fontSize = 20)
    graphics.drawText("Go here 👉", 360, 350, fontSize = 20)
    graphics.drawText("Level 1", 200, 0, fontSize = 15)
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
    if x > 450:
        # break out of the infinite loop to go to next level
        break

# level 2
x = 50
y = 100

while True:
    graphics.clear(0, 1, 0)
    graphics.drawText("Go here to win! 👉", 275, 350, fontSize = 20)
    graphics.drawText("Level 2", 200, 0, fontSize = 15)
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
    if x > 450:
        # break out of the infinite loop to go to end!
        break
    
# win game screen (or new level etc.)
graphics.clear(0, 0, 1)
graphics.drawText("You won!!!", 150, 200, fontSize = 30)
    
    