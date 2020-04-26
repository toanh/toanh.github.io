bg = Sprite("https://i.imgur.com/Ai5qELV.png", x = 0, y = 0)

money1 = TextSprite("💰", x = 450, y = 290)
pyangelo1 = Sprite("https://i.imgur.com/mtUAWTK.png", x = 525, y = 290)

money2 = TextSprite("💰", x = 5, y = 100)
pyangelo2 = Sprite("https://i.imgur.com/mH85TXk.png", x = -70, y = 100)

yellow = 1

#graphics.playSound("sounds/Turbo_Outrun_us_gold.mp3")

@loop_animation
yellow = yellow - 0.04
if yellow < 0:
    yellow = 1
    
money1.x = money1.x - 3
if money1.x < -50:
    money1.x = 500
    
money2.x = money2.x + 3
if money2.x > 500:
    money2.x = -50
    
pyangelo1.x = pyangelo1.x - 3
if pyangelo1.x < -50:
    pyangelo1.x = 500
    
pyangelo2.x = pyangelo2.x + 3
if pyangelo2.x > 500:
    pyangelo2.x = -50

graphics.drawSprite(bg)
graphics.drawSprite(money1)
graphics.drawSprite(money2)
graphics.drawSprite(pyangelo1)
graphics.drawSprite(pyangelo2)

graphics.drawText("River", x = 170, y = 200, fontSize = 35, r = 0.4, g = 0.4, b = 1)
graphics.drawText("Run", x = 260, y = 150, fontSize = 35, r = 0.4, g = 0.4, b = 1)

graphics.drawText("Insert Coin to Play!", x = 120, y = 20, fontSize = 25, r = yellow, g = yellow, b = 0)

