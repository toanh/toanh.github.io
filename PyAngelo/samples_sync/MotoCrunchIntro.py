graphics.playSound("sounds/Eliminator_intro.mp3")
#Cybernoid_II.mp3
#Afterburner_01.mp3
#Eliminator_intro.mp3

graphics.loadSound("http://beerpager.weebly.com/uploads/4/3/9/3/4393220/____________________beerpager-biker-sound.mp3")
#graphics.playSound(sound)
player = Sprite("https://i.imgur.com/EAZG2Qp.png?1", x =0, y=100)
background = Sprite("https://i.imgur.com/9cJY1xJ.png", x = 0, y = 0)
explosion = Sprite("https://i.imgur.com/T7ViH9Z.jpg", x =-50, y =-50)
text = "Moto Crash"
image = "https://i.imgur.com/T7ViH9Z.jpg"
crash = graphics.drawImage(image, 100, 100, 100, 100)
level = 0
b=1.0

@loop_animation

player.x = player.x + 1.6
player.y = player.y + 0.5

graphics.clear()
graphics.drawSprite(background)
graphics.drawSprite(player)
graphics.drawText("Level 1", 200, 370, fontSize=20, r=1, g=0, b = 0)

if player.x > 180 and player.x < 300:
    player.y = player.y - 4
    
elif player.x > 301 and player.x < 500:
    player.y = player.y - 1
    graphics.drawSprite(explosion)
    graphics.drawText("MOTO CRUNCH!", 20, 200, fontName="Arial Black", fontSize= 40, r=0, g=0, b = b)
    b = b - 0.01

elif player.x > 501:
    player.x = 0
    player.y = 100
    b = 1.0







