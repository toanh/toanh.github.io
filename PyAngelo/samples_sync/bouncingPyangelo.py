# set up sprite position and size
box_sprite = Sprite("https://pyangelo.github.io/PyAngelo.png", width = 64, height = 32, r = 1, g = 0, b = 0)

# set up box direction (and speed)
dir_x = 4
dir_y = 4

@loop_animation:
# update the position based on direction (and speed)
box_sprite.x += dir_x
box_sprite.y += dir_y

# check if the box passes the left edge
if box_sprite.x < 0:
    # snap it back to place
    box_sprite.x = 0
    # reverse direction
    dir_x *= -1
    
# check if the box passes the bottom edge
if box_sprite.y < 0:
    # snap it back to place
    box_sprite.y = 0
    # reverse direction
    dir_y *= -1
    
# check if the box passes the right edge
if box_sprite.x > graphics.width - box_sprite.getWidth():
    # snap it back to place
    box_sprite.x = graphics.width - box_sprite.getWidth()
    # reverse direction
    dir_x *= -1
    
# check if the box passes the top edge
if box_sprite.y > graphics.height - box_sprite.getHeight():
    # snap it back to place
    box_sprite.y = graphics.height - box_sprite.getHeight()
    # reverse direction
    dir_y *= -1

# clears the screen to black
graphics.clear(0.0, 0.0, 0.0, 1.0)
# draw the rectangle
graphics.drawSprite(box_sprite)
