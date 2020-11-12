graphics.clear(0, 0, 0)

turtle.speed(2)

for i in range(12):
    turtle.forward(50)
    turtle.left(90)
    
    turtle.forward(50)
    turtle.left(90)
    
    turtle.forward(50)
    turtle.left(90)
    
    turtle.forward(50)
    
    turtle.left(60)
    
graphics.drawText("All done!", 175, 80, fontSize = 30)