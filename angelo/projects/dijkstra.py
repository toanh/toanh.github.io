import math
i = 0
img = "https://vignette.wikia.nocookie.net/mario-ememiesbossesand-mario-with-a-power-up/images/0/0a/96px-SMB3_Smallmario.svg.png"
x = 0
y = 0

while True:
    colour = 0.5 * math.sin(i) + 0.5
    if graphics.isKeyPressed(KEY_D):
        x += 1
    if graphics.isKeyPressed(KEY_A):
        x -= 1
    if graphics.isKeyPressed(KEY_W):
        y += 1
    if graphics.isKeyPressed(KEY_S):
        y -= 1        
    graphics.clear(1,colour,0)
    
    graphics.drawImage(img, 100 + x, 100 + y )
    
    i += 0.05
    
    if i > 100 * 2 * math.pi:
        i = 0
        
    graphics.reveal()