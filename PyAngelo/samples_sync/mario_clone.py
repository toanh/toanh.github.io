# setting up the player

player = Sprite("https://i.imgur.com/mH85TXk.png", x = 0, y = 20)
#left facing image: https://i.imgur.com/mtUAWTK.png
#right facing image: https://i.imgur.com/mH85TXk.png
player.y_dir = 0
player.x_dir = 0
player.score = 0
player.lives = 1
player.can_jump = False

# list of floors (horizontal)
floors = []
ground = Sprite(Rectangle(0, 0, 750, 20), r=0.5, g=1, b=0.5)
plat01 = Sprite(Rectangle(300, 100, 100, 20), r=0.5, g=1, b=0.5)
plat02 = Sprite(Rectangle(200, 200, 100, 20), r=0.5, g=1, b=0.5)
floors.append(ground)
floors.append(plat01)
floors.append(plat02)

# list of walls (vertical)
walls = []
walls.append(Sprite("https://i.imgur.com/VqmtsEo.png", x = 450, y = 20, r = 0, g = 0, b = 1))
walls.append(Sprite(Rectangle(600, 20, 150, 20), x = 450, y = 20, r = 0.2, g = 0.2, b = 1))
walls.append(Sprite(Rectangle(620, 40, 130, 20), x = 450, y = 20, r = 0.3, g = 0.3, b = 1))
walls.append(Sprite(Rectangle(640, 60, 110, 20), x = 450, y = 20, r = 0.4, g = 0.4, b = 1))
walls.append(Sprite(Rectangle(660, 80, 90, 20), x = 450, y = 20, r = 0.5, g = 0.5, b = 1))
walls.append(Sprite(Rectangle(680, 100, 70, 20), x = 450, y = 20, r = 0.6, g = 0.6, b = 1))
walls.append(Sprite(Rectangle(700, 120, 50, 20), x = 450, y = 20, r = 0.7, g = 0.7, b = 1))

# list of collectibles
collects = []
collects.append(Sprite("https://i.imgur.com/jgIxuG7.png", 100, 100))
collects.append(Sprite("https://i.imgur.com/jgIxuG7.png", 200, 240))
collects.append(Sprite("https://i.imgur.com/jgIxuG7.png", 350, 140))
collects.append(Sprite("https://i.imgur.com/jgIxuG7.png", 720, 160))


# list of enemies
enemies = []
en01 = TextSprite("😈", x=200,y=220)
en01.y_dir = -1
en01.x_dir = 1
enemies.append(en01)
en02 = TextSprite("👻", x=500,y=20)
en02.y_dir = -1
en02.x_dir = 1
enemies.append(en02)
en03 = TextSprite("😾", x=580, y=20)
en03.y_dir = -1
en03.x_dir = 1
enemies.append(en03)

@loop_animation
graphics.clear(0, 0.5, 1.0)
while graphics.loadingResources > 0:
    graphics.drawText("Loading resources..", 0, 0)
    return

# checking game state
if player.lives > 0:
    # player is still alive.. keep playing
    
    # checking controls
    if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
        player.x += 2
        player.x_dir = 1
        player.image = "https://i.imgur.com/mH85TXk.png"
    if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
        player.x -= 2
        player.x_dir = -1
        player.image = "https://i.imgur.com/mtUAWTK.png"
    if (graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP)) and player.can_jump:
        player.y_dir += 15
    
    player.can_jump = False
    # checking interaction with walls
    for wall in walls:
        if player.overlaps(wall):
            # player lands on top of the wall?
            if player.y_dir < 0:
                if player.y > wall.y + wall.height - player.y/2:
                    player.y = wall.y + wall.height
                    player.y_dir = 0
                    player.can_jump = True
            # player is overlapping the left of the wall and moving right
            elif player.x_dir < 0 and player.y < wall.y + wall.height - player.y/2:
                player.x = wall.x + wall.width
            # player is overlapping the right of the wall and moving left
            elif player.x_dir > 0 and player.y < wall.y + wall.height - player.y/2:
                player.x = wall.x - player.width
            player.x_dir = 0
        # checking enemies and walls
        for enemy in enemies:
            if enemy.overlaps(wall):
                # enemy reverses horizontal direction if the bump into a wall
                if enemy.x_dir < 0:
                    enemy.x = wall.x + wall.width
                else:
                    enemy.x = wall.x - enemy.width
                enemy.x_dir = -enemy.x_dir
                
    # apply gravity (accerelating downward speed) to the player
    player.y_dir -= 1
    player.y += player.y_dir
    
    # apply gravity and moving enemies    
    for enemy in enemies:
        enemy.y_dir -= 1
        enemy.x += enemy.x_dir
        enemy.y += enemy.y_dir
    
    # checking interaction with floors
    for floor in floors:
        # does player land on a floor?
        if player.overlaps(floor) and player.y_dir < 0:
            player.y = floor.y + floor.height
            player.y_dir = 0
            player.can_jump = True
        # does the enemy land on a floor?
        for enemy in enemies:
            if enemy.overlaps(floor) and enemy.y_dir < 0:
                enemy.y = floor.y + floor.height
                enemy.y_dir = 0

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
            else:
                # player loses life if s/he contacts the enemy but didn't land on it
                player.lives -= 1
        n += 1

    # not using a for loop because we may be deleting elements from the list
    # using indexed elements instead        
    n = 0
    while n < len(collects):
        # player overlaps a collectible!
        if player.overlaps(collects[n]):
            del collects[n]
            player.score += 10
        n += 1
        
    offsetX = 0
    if player.x > graphics.width / 2:
        offsetX = player.x -graphics.width / 2
    # draw all the level elements in turn
    for floor in floors:
        graphics.drawSprite(floor, offsetX)
        
    for wall in walls:
        graphics.drawSprite(wall, offsetX)        
        
    for collect in collects:
        graphics.drawSprite(collect, offsetX)    
        
    for enemy in enemies:
        graphics.drawSprite(enemy, offsetX)       
        
    # player is drawn last so that s/he appears on top of everything
    graphics.drawSprite(player, offsetX)
else:
    # player is dead, draw end text
    graphics.drawText("GAME OVER!", 200, 200, r  = 1)