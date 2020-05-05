# Flappy Birds by Mr Del Vecchio

background = Sprite("https://i.imgur.com/HAPgqEz.png", x = 0, y=0)
player_up = Sprite("https://i.imgur.com/6eQatQy.png", x = 250 -64, y = 200 - 48)
player = Sprite("https://i.imgur.com/OBWOs0G.png", x = 250 -64, y = 200 - 48)

pipe_ground = Sprite(Rectangle(400, 20, 40, 200), r = 0, g = 1, b = 0)
pipe_top = Sprite(Rectangle(500, 300, 40, 200), r = 0, g = 1, b = 0)
graphics.drawSprite(background)
score = 0


@loop_animation
graphics.drawSprite(background)

# if the 'W' is pressed update the x coordinate to move 3 pixel up
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    player.y = player.y + 3
    player.image = "https://i.imgur.com/6eQatQy.png"
    
# if the 'S' is pressed update the x coordinate to move 3 pixel down
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    graphics.drawSprite(player)
    player.y = player.y - 3
    player.image = "https://i.imgur.com/OBWOs0G.png"
else:
    graphics.drawSprite(player)
    
#player
player.y = player.y - 2
#if player.y < 0:
 #   player.y = 400
    
#pipes
pipe_ground.x = pipe_ground.x - 1
pipe_top.x = pipe_top.x - 1
pipe_ground.x = pipe_ground.x - 1
pipe_top.x = pipe_top.x - 1
if pipe_ground.x < 0:
    pipe_ground.x = 600
    score += 10
    
if pipe_top.x < 0:
    pipe_top.x = 700
    score += 10

graphics.drawSprite(pipe_ground)
graphics.drawSprite(pipe_top)
graphics.drawText("Score: " + str(score), 200, 370, fontSize=20)