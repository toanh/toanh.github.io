graphics.playSound("sounds/Turbo_Outrun_03.mp3")
coinSound = graphics.loadSound("sounds/coin.mp3")
speedSound = graphics.loadSound("sounds/speed.mp3")

# facing right image for player
player = Sprite("https://i.imgur.com/mH85TXk.png", 220, 376)
player.speed = 1
player.lives = 1
player.score = 0

# level height
level_height = 500 * 16
# level image height
level_image_height = 1024
level_image_width = 64

# initial location of level image to be drawn
# (at the very top of the image - ready to scroll down)
scroll_y = level_height - graphics.height
# how fast the level scrolls
scroll_speed = 2

pickups = []
pickups.append(TextSprite("💰", x=24, y = 75))
pickups.append(TextSprite("💰", x=24, y = 75))
pickups.append(TextSprite("💰", x=8, y = 305))
pickups.append(TextSprite("💰", x=38, y = 317))
pickups.append(TextSprite("💰", x=40, y = 545))
pickups.append(TextSprite("💰", x=30, y = 774))
pickups.append(TextSprite("💰", x=10, y = 922))
pickups.append(TextSprite("💨", x = 24, y = 183))

# adjust all the pickup positions
for pickup in pickups:
    pickup.x = (pickup.x/ level_image_width) * graphics.width
    pickup.y =  graphics.height -(pickup.y / level_image_height) * level_height
    
@loop_animation
scroll_y -= scroll_speed

for pickup in pickups:
    pickup.y += scroll_speed

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
    graphics.drawImage("samples_sync/river_level.png", 0, y = -scroll_y, width = 500, height = 500 * 16)
    
    # get pixel colour at the centre of the player sprite
    colour = graphics.getPixelColour(player.x + player.width/2, player.y + player.height/2)
    if colour.r == 136/255.0 and colour.b == 21/255.0 and colour.g == 0:
        player.lives -= 1
        
    i = 0
    while i < len(pickups):
        pickup = pickups[i]    
        if player.overlaps(pickup):
            if pickup.image.text == "💰":
                player.score += 10
                graphics.playSound(coinSound)
            if pickup.image.text == "💨":
                player.speed = 1.5 
                graphics.playSound(speedSound)
            del pickups[i]
        i += 1

    for pickup in pickups:
        graphics.drawSprite(pickup)
        
    graphics.drawSprite(player)
    graphics.drawText(f"Score: {int(player.score)}", 0, 380)