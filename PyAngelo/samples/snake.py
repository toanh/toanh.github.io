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
                     (x+1) * block_width, \
                     (height - (y+1)) * block_height,
                     r, g, b, a)

# setting up the screen
width = 30
height = 20

block_width = 16
block_height = 16

speed = 1

# Initializing values
score = 0
scroll = 0
scroll_win = 11
# Initial snake co-ordinates
direction = [speed, 0]
snake = [[4,5], [4,5], [4,5]]
food = [20,10]    



playing = True

while playing:
    graphics.clear()

    score +=1
    
    # check for keys
    if graphics.isKeyPressed(KEY_D):
      direction = [1, 0]
    elif graphics.isKeyPressed(KEY_A):
        direction = [-1, 0]
    elif graphics.isKeyPressed(KEY_W):
      direction = [0, -1]
    elif graphics.isKeyPressed(KEY_S):
      direction = [0, 1]      
    
    # save last pos of snake
    #screen.printAt(' ', snake[-1][0], snake[-1][1])
       
    # move the snake body
    for n in range(len(snake) - 1, 0, -1):
      snake[n][0] = snake[n - 1][0]
      snake[n][1] = snake[n - 1][1]      
    
      # move snake head
    snake[0][0] += direction[0]
    snake[0][1] += direction[1]
    
    # snake wraps around the screen edges
    if snake[0][0] <= 0: 
      snake[0][0] = width - 2
    if snake[0][1] <= 0: 
      snake[0][1] = height - 2
    if snake[0][0] >= width - 1: 
      snake[0][0] = 1
    if snake[0][1] >= height - 1: 
      snake[0][1] = 1    
    
    # draw food
    drawBlock(food[0], food[1], 1, 0, 0)
    #screen.printAt('*', food[0], food[1])
      
    # draw snake
    for n, body in enumerate(snake):
      #symbol = "#"
      #screen.printAt(symbol, body[0], body[1])
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
        food = [randint(1, width-2), randint(1, height-2)] 
    graphics.sleep(50)
