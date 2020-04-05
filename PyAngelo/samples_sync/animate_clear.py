green = 0

@loop_animation
# increase the green amount a litte bit
green = green + 0.01

# if max'ed out, then reset it to black
if green > 1.0:
    green = 0

# clear the screen using the green variable
graphics.clear(0.0, green, 0.0, 1.0)           

