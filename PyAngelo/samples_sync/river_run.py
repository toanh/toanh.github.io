graphics.playSound("sounds/mario.mp3")

# facing right image for player
player = Sprite("https://i.imgur.com/mH85TXk.png", 220, 376)

player.speed = 1
player.lives = 1
player.score = 0

# initial location of image to be draw (at the very top of the image - ready to scroll down)
scroll_y = 500 * 16 - 400

scroll_speed = 2

@loop_animation
scroll_y -= scroll_speed

if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    player.x = player.x - player.speed
    # change image for player depending on direction moved
    player.image = "https://i.imgur.com/mtUAWTK.png"
    
# if the 'D' is pressed update the x coordinate to move 1 pixel right
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    player.x = player.x + player.speed
    # change image for player depending on direction moved
    player.image = "https://i.imgur.com/mH85TXk.png"
    
# if the 'W' is pressed update the x coordinate to move 1 pixel up
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    player.y = player.y + player.speed
    
# if the 'S' is pressed update the x coordinate to move 1 pixel down
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    player.y = player.y - player.speed
    
# keep player within top/bottom borders
if player.y < 0:
    player.y = 0
elif player.y > graphics.height - player.height:
    player.y = graphics.height - player.height
    
graphics.clear()
if player.lives <= 0:
    graphics.drawText(f"You crashed!!!", 127, 167, fontSize = 28, r = 1, g = 0, b = 0)
    graphics.drawText(f"You crashed!!!", 130, 170, fontSize = 28, r = 1, g = 1, b = 1)
    graphics.drawText(f"Score: {int(player.score)}", 0, 380)
elif scroll_y <= 0:
    # end of level
    graphics.drawText(f"You won!!!", 157, 167, fontSize = 28, r = 0, g = 1, b = 0)
    graphics.drawText(f"You won!!!", 160, 170, fontSize = 28, r = 1, g = 1, b = 1)
    graphics.drawText(f"Score: {int(player.score)}", 0, 380)
else:    
    player.score += 0.1
    # draws the level image stretched out (image is only 64 x 1024) but wil be stretched
    # to 500 x 40,000 - conserves memery at the expense of pixel blurriness/aliasing
    graphics.drawImage("samples_sync/level01.png", 0, y = -scroll_y, width = 500, height = 500 * 16)
    
    # get pixel colour at the centre of the player sprite
    colour = graphics.getPixelColour(player.x + player.width/2, player.y + player.height/2)
    if colour.r == 136/255.0 and colour.b == 21/255.0 and colour.g == 0:
        player.lives -= 1
    ###### bonuses! - doesn't disappear, just a check of background colour
    # can add sound effect to improve feedback, however, must be triggered upon collection
    # entry otherwise sound effects will keep echo'ing
    elif colour.r == 181/255.0 and colour.b == 29/255.0 and colour.g == 230/255.0:
        # speed boost
        player.speed = 1.5        
        graphics.drawText(f"Speed boost!", 167, 167, fontSize = 20, r = 1, g = 1, b = 1)
    elif colour.r == 255/255.0 and colour.b == 0/255.0 and colour.g == 242/255.0:
        # points bonus
        player.score += 10
        graphics.drawText(f"Points bonus!", 167, 167, fontSize = 20, r = 1, g = 1, b = 1)

    graphics.drawSprite(player)
    graphics.drawText(f"Score: {int(player.score)}", 0, 380)