from pyangelo import *
from random import *

blockSize = 20
font = str(blockSize) + "px consolas"

score = 0
gameState = 'intro'

print(GREEN + HL_RED + "SNAKE " + RED + HL_GREEN + "GAME")

label .here
clearScreen()
drawText("Snake!", 120, 40, font, RED)
drawText("Score: " + str(score), 100, 65, font)

# draw the border
drawRect(18, 98, \
         290, 428, 1, GREEN)    

if gameState == 'intro':
    drawText("Press 'ENTER' to start", 40, 285, font)
    if isKeyReleased('Enter'):
        gameState = 'play'
        # Initializing values
        score = 0
        speed = 0.0005
        
        # Initial snake co-ordinates
        snake = [[4 * blockSize, 15 * blockSize], \
                 [3 * blockSize ,15 * blockSize], \
                 [2 * blockSize, 15 * blockSize]]
        food = [7 * blockSize, 13 * blockSize]    
        dx = 1
        dy = 0
        progress = 0            
elif gameState == 'play':
    # check for keys
    if isKeyPressed('d'):
        dx = 1
        dy = 0
    elif isKeyPressed('a'):
        dx = -1
        dy = 0
    elif isKeyPressed('s'):
        dx = 0
        dy = 1
    elif isKeyPressed('w'):
        dx = 0
        dy = -1
    progress = progress + speed
    if progress >= 1.0:
        progress = 1.0 - progress
        # move the snake body
        for n in range(len(snake) - 1, 0, -1):
          snake[n][0] = snake[n - 1][0]
          snake[n][1] = snake[n - 1][1]      
        snake[0][0] = snake[0][0] + dx * blockSize
        snake[0][1] = snake[0][1] + dy * blockSize

    # draw food
    drawText("🍓", food[0], food[1], font)
    # draw head
    drawText("😀", snake[0][0], snake[0][1], font)
    # draw body
    for n, body in enumerate(snake[1:]):
        drawText("📀", body[0], body[1], font)

    if snake[0][0] <= 18 or \
      snake[0][1] <= 100 or \
      snake[0][0] >= 300 or \
      snake[0][1] >= 523: 
        gameState = 'intro'            

    # did the snake eat itself?
    if snake[0] in snake[1:]:
        gameState = 'intro'
    
    # snake eats food
    if snake[0] == food:
      # grow snake
      snake.append([snake[-1][0], snake[-1][1]])
      score += 100
      speed += 0.00025
      # generate new food
      # can't be located in the snake
      while food in snake:
        foodX = randint(1, 14) * blockSize
        foodY = randint(6, 26) * blockSize
        food = [foodX, foodY]         
goto .here