# set up box position and size
x = 0
y = 0
width = 32
height = 32

# set up box direction (and speed)
dir_x = 4
dir_y = 4

# loop forever
while True:
    
    # update the position based on direction (and speed)
    x = x + dir_x
    y = y + dir_y
    
    # check if the box passes the left edge
    if x < 0:
        # snap it back to place
        x = 0
        # reverse direction
        dir_x *= -1
        
    # check if the box passes the bottom edge
    if y < 0:
        # snap it back to place
        y = 0
        # reverse direction
        dir_y *= -1
        
    # check if the box passes the right edge
    if x > graphics.width - width:
        # snap it back to place
        x = graphics.width - width
        # reverse direction
        dir_x *= -1
        
    # check if the box passes the top edge
    if y > graphics.height - height:
        # snap it back to place
        y = graphics.height - height
        # reverse direction
        dir_y *= -1
    
    # clears the screen to black
    graphics.clear(0.0, 0.0, 0.0, 1.0)
    # draw the rectangle
    graphics.drawRect(x, y, x + width, y + height, 1, 0, 0)
    