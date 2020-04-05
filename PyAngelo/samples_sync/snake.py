############## SNAKE GAME ##############
#
# Instructions:
#  1) Use the 'w', 'a', 's', 'd' keys to 
#     move the snake
#  2) Aim to eat the '*' food
#  3) The game ends when the snake 
#     doubles back on itself
#
# Activities:
#  1) Change the scrolling text at the top
#  2) Change the symbols for the snake or 
#     its food (change the #  or * to 
#     another symbol)
#
########################################

from random import *

def drawBlock(x, y, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
    graphics.drawRect(x * block_width, \
                     (height - y) * block_height, \
                     block_width, \
                     block_height,
                     r, g, b, a)

# setting up the screen
width = 25
height = 20

block_width = 20
block_height = 20

speed = 1

# Initializing values
score = 0
scroll = 0
scroll_win = 11
# Initial snake co-ordinates
direction = [speed, 0]
snake = [[4,5], [4,5], [4,5]]
food = [20,10]    

graphics.clear()

playing = True

@loop_animation
if not playing: 
    graphics.drawText("Game Over!", 150, 190, fontSize = 30)
else:
    score += 5
    # check for keys
    if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
      direction = [1, 0]
    elif graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
        direction = [-1, 0]
    elif graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
      direction = [0, -1]
    elif graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
      direction = [0, 1]      
    
    # save last pos of snake
    drawBlock(snake[-1][0], snake[-1][1], 0, 0, 0)
       
    # move the snake body
    for n in range(len(snake) - 1, 0, -1):
      snake[n][0] = snake[n - 1][0]
      snake[n][1] = snake[n - 1][1]      
    
      # move snake head
    snake[0][0] += direction[0]
    snake[0][1] += direction[1]
    
    # snake dies if it touches the edge
    if snake[0][0] < 0: 
      playing = False
    if snake[0][1] < 0: 
      playing = False
    if snake[0][0] >= width: 
      playing = False
    if snake[0][1] >= height: 
      playing = False    
    
    # show score  
    graphics.drawRect(200, 370, 300, 30, 0, 0, 0)
    graphics.drawText("Score: "  + str(score), 200, 370, fontSize = 15)          
    
    # draw food
    drawBlock(food[0], food[1], 1, 0, 0)

    # draw snake
    for n, body in enumerate(snake):
      drawBlock(body[0], body[1], 0, 1, 0)
      
    # snake ate itself
    if snake[0] in snake[1:]:
      playing = False
    
    # snake eats food
    if snake[0] == food:
      # grow snake
      snake.append([snake[-1][0], snake[-1][1]])
      score += 100
    
      # generate new food
      # can't be located in the snake
      while food in snake:
        food = [randint(0, width), randint(0, height)] 
    
    graphics.sleep(50)
