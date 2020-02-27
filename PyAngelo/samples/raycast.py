# Adapted from: https://github.com/oscr/PyRay/blob/master/pyray.py
# Credits to the original author below

"""
The MIT License (MIT)
Copyright (c) 2013 Oscar Utbult
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
""" 

import math

# A map over the world
worldMap =  [
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
            [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

# Creates window 
WIDTH = 250
HEIGHT = 200

showShadow = True

# Defines starting position and direction
positionX = 3.0
positionY = 7.0

directionX = 1.0
directionY = 0.0

planeX = 0.0
planeY = 0.5

# Movement constants   
ROTATIONSPEED = 0.05
MOVESPEED = 0.05

# Trigeometric tuples + variables for index
TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
COS, SIN = (0,1)

while True:

    # Checks with keys are pressed by the user
    # Uses if so that more than one button at a time can be pressed.  

    if graphics.isKeyPressed(KEY_A):
        oldDirectionX = directionX
        directionX = directionX * ITGM[COS] - directionY * ITGM[SIN]
        directionY = oldDirectionX * ITGM[SIN] + directionY * ITGM[COS]
        oldPlaneX = planeX
        planeX = planeX * ITGM[COS] - planeY * ITGM[SIN]
        planeY = oldPlaneX * ITGM[SIN] + planeY * ITGM[COS]

    if graphics.isKeyPressed(KEY_D):
        oldDirectionX = directionX
        directionX = directionX * TGM[COS] - directionY * TGM[SIN]
        directionY = oldDirectionX * TGM[SIN] + directionY * TGM[COS]
        oldPlaneX = planeX
        planeX = planeX * TGM[COS] - planeY * TGM[SIN]
        planeY = oldPlaneX * TGM[SIN] + planeY * TGM[COS]    

    if graphics.isKeyPressed(KEY_W):
        if not worldMap[int(positionX + directionX * MOVESPEED)][int(positionY)]:
            positionX += directionX * MOVESPEED
        if not worldMap[int(positionX)][int(positionY + directionY * MOVESPEED)]:
            positionY += directionY * MOVESPEED
            
    if graphics.isKeyPressed(KEY_S):
        if not worldMap[int(positionX - directionX * MOVESPEED)][int(positionY)]:
            positionX -= directionX * MOVESPEED
        if not worldMap[int(positionX)][int(positionY - directionY * MOVESPEED)]:
            positionY -= directionY * MOVESPEED

    showShadow = True

    # Draws roof and floor
    graphics.clear(0.2, 0.2, 0.2)
    
    graphics.drawRect(WIDTH/2, HEIGHT, WIDTH * 1.5, HEIGHT * 1.5, 0, 0.5, 1)
    graphics.drawRect(WIDTH/2, HEIGHT/2, WIDTH * 1.5, HEIGHT, 0.6, 0.15, 0.15)


    graphics.drawText("Use the W,A,S,D keys to move", 140, 80, fontSize = 12)
    # Starts drawing level from 0 to < WIDTH 
    column = 0        
    while column < WIDTH:
        cameraX = 2.0 * column / WIDTH - 1.0
        rayPositionX = positionX
        rayPositionY = positionY
        rayDirectionX = directionX + planeX * cameraX
        rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

        # In what square is the ray?
        mapX = int(rayPositionX)
        mapY = int(rayPositionY)

        # Delta distance calculation
        # Delta = square ( raydir * raydir) / (raydir * raydir)
        deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
        deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))

        # We need sideDistanceX and Y for distance calculation. Checks quadrant
        if (rayDirectionX < 0):
            stepX = -1
            sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

        else:
            stepX = 1
            sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

        if (rayDirectionY < 0):
            stepY = -1
            sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

        else:
            stepY = 1
            sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

        # Finding distance to a wall
        hit = 0
        while  (hit == 0):
            if (sideDistanceX < sideDistanceY):
                sideDistanceX += deltaDistanceX
                mapX += stepX
                side = 0
                
            else:
                sideDistanceY += deltaDistanceY
                mapY += stepY
                side = 1
                
            if (worldMap[mapX][mapY] > 0):
                hit = 1

        # Correction against fish eye effect
        if (side == 0):
            perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
        else:
            perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)

        # Calculating HEIGHT of the line to draw
        lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))
        drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0

        # if drawStat < 0 it would draw outside the screen
        if (drawStart < 0):
            drawStart = 0

        drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0

        if (drawEnd >= HEIGHT):
            drawEnd = HEIGHT - 1

        # Wall colors 0 to 3
        wallcolors = [ [], [0.75, 0, 0], [0, 0.75, 0], [0, 0, 0.75] ]
        color = wallcolors[ worldMap[mapX][mapY] ]                                  

        # If side == 1 then ton the color down. Gives a "showShadow" an the wall.
        # Draws showShadow if showShadow is True
        if showShadow:
            if side == 1:
                for i,v in enumerate(color):
                    color[i] = (v / 1.5)                    

        # Drawing the graphics   
        graphics.drawLine(WIDTH/2 + column, HEIGHT/2 + drawStart, WIDTH/2 + column, HEIGHT/2 + drawEnd, color[0], color[1], color[2], 1, 8)

        column += 8