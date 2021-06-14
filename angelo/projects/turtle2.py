graphics.clear(0, 0, 0)

turtle.show()
turtle.speed(5)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

import math
b = 0
while True:
    # clearing the graphics independent of the turtle
    # i.e. the turtle drawing remains
    graphics.clear(0, math.sin(b) * 0.5 + 0.5, 1) 
    b += 0.05
    graphics.drawText("Press 'A' to continue", 50, 100, fontSize = 30)
    
    if graphics.isKeyPressed(KEY_A):
        break    
    
graphics.clear(0, 0, 1) 
graphics.drawText("🐢", 250, 175, fontSize = 20)    

# clearing the turtle independent of the graphics
# i.e. the background remains
turtle.clear()

turtle.pencolor(255, 0, 255)
turtle.fillcolor(255, 0, 0, 64)
        
turtle.begin_fill()
turtle.forward(35)
turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.forward(35)
turtle.end_fill()
graphics.drawText("All done!", 150, 100, fontSize = 30)