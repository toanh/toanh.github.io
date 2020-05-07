# start with the music!
music = graphics.loadSound("sounds/Cybernoid_II.mp3")
graphics.playSound(music, loop = True, volume = 0.3)

# loading the images
playerRight = "https://i.imgur.com/mH85TXk.png"
playerLeft = "https://i.imgur.com/mtUAWTK.png"
pipeImage = "https://i.imgur.com/VqmtsEo.png"
cherryImage = "https://i.imgur.com/jgIxuG7.png"

graphics.loadImage(playerLeft)
graphics.loadImage(playerRight)
graphics.loadImage(pipeImage)
graphics.loadImage(cherryImage)

level_width = 700

# setting up the player
player = Sprite(playerRight, x = 0, y = 20)
player.y_dir = 0
player.x_dir = 0
player.score = 0
player.health = 1
player.can_jump = False

# list of floors (solid from the top only - can jump on them from underneath)
floors = []
# the main floor
floors.append(Sprite(Rectangle(0, 0, level_width, 20), r = 0.5, g = 1, b = 0.5))
# a sample floor
floors.append(Sprite(Rectangle(180, 180, 100, 20), r = 0.5, g = 1, b = 0.5))

# list of blocks (fully solid)
walls = []
# walls at the left/right edges to prevent falling off level
walls.append(Sprite(Rectangle(-1, 0, 1, 1000), r = 0.7, g = 0.7, b = 1))
walls.append(Sprite(Rectangle(level_width, 0, 1, 1000), r = 0.7, g = 0.7, b = 1))

# a pipe block
walls.append(Sprite(pipeImage, x = 100, y = 20, r = 0, g = 0, b = 1))
# sample block
walls.append(Sprite(Rectangle(100, 120, 20, 20), r = 0.2, g = 0.2, b = 1))

# list of collectibles
collects = []
collects.append(Sprite(cherryImage, 100, 200))
final = TextSprite("🍉", x = level_width - 50, y = 120)
final.type = 3  # type of 3 means the level completion collectible
collects.append(final)

# list of enemies
enemies = []
en01 = TextSprite("😈", x = 200, y = 220)
en01.y_dir = -1
en01.x_dir = 1
enemies.append(en01)







################################################################################
# Students: you don't need to worry too much about the code under here, it's   #
# for the physics and collision detection.                                     #
#                                                                              #
# Those who need to customise and tweak things are welcome to have go at       #
# changing the code and settings though.                                       #
################################################################################

# only show loading resources screen during the initial batch of loads
isFirstTime = True
won = False

@loop_animation

graphics.clear(0, 0.5, 1.0)

while graphics.loadingResources > 0 and isFirstTime:
    graphics.drawText("Loading resources... " + str(graphics.loadingResources) + " remaining.", 0, 0)
    return
isFirstTime = False

if won:
    # player has won!
    graphics.clear()
    graphics.drawText("YOU WON!", 220, 200)
    graphics.drawText(f"Score: {player.score}",225,160)
# checking game state
elif player.health > 0:
    # player is still alive.. keep playing
    
    old_x = player.x
    old_y = player.y

    # checking controls
    if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
        player.x += 2
        player.x_dir = 1
        player.setData(playerRight)
    if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
        player.x -= 2
        player.x_dir = -1
        player.setData(playerLeft)
    if (graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP) or graphics.isKeyPressed(KEY_V_FIRE)) and player.can_jump:
        player.y_dir += 15
    
    #if apply_gravity:
        # apply gravity (accerelating downward speed) to the player
    player.y_dir -= 1
    player.y += player.y_dir
    
    player.can_jump = False
    
    # apply gravity and moving enemies    
    for enemy in enemies:
        enemy.y_dir -= 1
        enemy.x += enemy.x_dir
        enemy.y += enemy.y_dir
        
    # checking interaction with floors
    for floor in floors:
        # does player land on a floor?
        if player.overlaps(floor) and player.y_dir < 0 and old_y > floor.y + floor.getHeight() - 1:
            player.y = floor.y + floor.getHeight()
            player.y_dir = 0
            player.can_jump = True
        # does the enemy land on a floor?
        for enemy in enemies:
            if enemy.overlaps(floor) and enemy.y_dir < 0:
                enemy.y = floor.y + floor.getHeight()
                enemy.y_dir = 0
    
    # checking interaction with walls
    for wall in walls:

        if player.overlaps(wall):
            # player bumps the bottom of the wall with head
            if player.y_dir > 0:
                if old_y + player.getHeight() < wall.y + 1:
                    # don't apply gravity if we've already corrected the vertical
                    # position
                    #apply_gravity = False
                    player.y = wall.y - player.getHeight()
                    player.y_dir = 0
                    
            if wall.type != 1:                        
                # player lands on top of the wall?
                if player.y_dir < 0:
                    if old_y > wall.y + wall.getHeight() - 1:
                        # don't apply gravity if we've already corrected the vertical
                        # position
                        #apply_gravity = False
                        player.y = wall.y + wall.getHeight()
                        player.y_dir = 0
                        player.can_jump = True
                        
                # player is overlapping the left of the wall and moving right
                if player.x_dir < 0 and old_x > wall.x + wall.getWidth() - 1:
                    player.x = wall.x + wall.getWidth() 
                    player.x_dir = 0
                # player is overlapping the right of the wall and moving left
                elif player.x_dir > 0 and old_x + player.getWidth()  < wall.x + 1:
                    player.x = wall.x - player.getWidth() 
                    player.x_dir = 0
            
        # checking enemies and walls
        for enemy in enemies:
            if enemy.overlaps(wall):
                if enemy.y_dir < 0:
                    enemy.y = wall.y + wall.getHeight()
                    enemy.y_dir = 0
                else:
                    # enemy reverses horizontal direction if the bump into a wall
                    if enemy.x_dir < 0:
                        enemy.x = wall.x + wall.getWidth() 
                    else:
                        enemy.x = wall.x - enemy.getWidth() 
                    enemy.x_dir = -enemy.x_dir
    

                
    # not using a for loop because we may be deleting elements from the list
    # using indexed elements instead
    n = 0
    while n < len(enemies):
        if player.overlaps(enemies[n]):
            # has the player landed on an enemy?
            if player.y_dir < 0:
                # kill it!
                del enemies[n]
                player.score += 10
                # bounce the player up a little
                player.y_dir = 10
            else:
                # player loses life if s/he contacts the enemy but didn't land on it
                player.health -= 1
        n += 1

    # not using a for loop because we may be deleting elements from the list
    # using indexed elements instead        
    n = 0
    while n < len(collects):
        # player overlaps a collectible!
        if player.overlaps(collects[n]):
            if collects[n].type == 3:
                won = True
            del collects[n]
            player.score += 10
        n += 1
        
    # fell off the level
    if player.y < 0:
        player.health = 0
        
    offsetX = 0
    if player.x > graphics.width / 2:
        offsetX = player.x -graphics.width / 2
    if player.x > level_width - graphics.width/2:
        offsetX = level_width - graphics.width
    # draw all the level elements in turn
    for floor in floors:
        graphics.drawSprite(floor, offsetX)
        
    for wall in walls:
        
        if wall.type != 1:
            # don't draw hidden blocks!
            graphics.drawSprite(wall, offsetX)        
        
    for collect in collects:
        graphics.drawSprite(collect, offsetX)    
        
    for enemy in enemies:
        graphics.drawSprite(enemy, offsetX)       
        
    # player is drawn last so that s/he appears on top of everything
    graphics.drawSprite(player, offsetX)
    
    graphics.drawText(f"Score: {player.score}",0,380)
    graphics.drawText(f"Health: {player.health}",440,380)
else:
    # player is dead, draw end text
    graphics.drawText("GAME OVER!", 200, 200, r  = 1)
    graphics.stopSound(music)
