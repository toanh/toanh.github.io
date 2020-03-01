import random

class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 32
        
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 1
        
        self.speed = 1
        
    def draw(self):
        graphics.drawRect(self.x, self.y, self.x + self.width, self.y + self.height, \
                            self.r, self.g, self.b, self.a)    
        
class Player (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 0
        self.g = 1
        self.b = 0
        
        self.cool_down = 10
        self.cool_down_timer = self.cool_down

    def update(self):
        self.cool_down_timer -= 1
        if self.cool_down_timer < 0:
            self.cool_down_timer = self.cool_down
            
        if graphics.isKeyPressed(KEY_A):
            self.x -= 1
        if graphics.isKeyPressed(KEY_D):
            self.x += 1
        if graphics.isKeyPressed(KEY_W):
            self.y += 1
        if graphics.isKeyPressed(KEY_S):
            self.y -= 1
            
        if graphics.isKeyPressed(KEY_J) and self.cool_down_timer == self.cool_down:
            newBullet = Bullet()
            newBullet.x = self.x
            newBullet.y = self.y
            bullets.append(newBullet)
            
        
class Bullet (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 1
        self.g = 0
        self.b = 0      
        
        self.speed = 10
        
        self.width = 8
        self.height = 8

    def update(self):
        self.y += self.speed
     
class Enemy (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 0
        self.g = 0
        self.b = 1      
        
        self.speed = -2
        
        self.width = 32
        self.height = 32

    def update(self):
        self.y += self.speed    
    

player = Player()
bullets = []
enemies = []
spawnTime = 50
spawnTimer = spawnTime

while True:
    graphics.clear(0, 0, 0)
    
    spawnTimer -= 1
    if spawnTimer < 0:
        spawnTimer = spawnTime
        newEnemy = Enemy()
        newEnemy.x = random.randint(0, graphics.width - newEnemy.width)
        newEnemy.y = graphics.height + newEnemy.height
        enemies.append(newEnemy)

    for bullet in bullets:
        if bullet.y > graphics.height:
            bullets.remove(bullet)

    for enemy in enemies:
        if enemy.y < -enemy.height:
            enemies.remove(enemy)    
            
    for bullet in bullets:
        for enemey in enemies:
            
            if graphics.overlaps(bullet.x, bullet.y, bullet.width, bullet.height, enemy.x, enemy.y, enemy.width, enemy.height):
                # collision!
                enemies.remove(enemy)
                bullets.remove(bullet)
                print("asdf")
                
                break
            
    for enemey in enemies:
        if graphics.overlaps(player.x, player.y, player.width, player.height, enemy.x, enemy.y, enemy.width, enemy.height):
            # collision!
            enemies.remove(enemy)
            print("asdf")
            
            continue            

    for bullet in bullets:
        bullet.update()
        bullet.draw()
        
    for enemy in enemies:
        enemy.update()
        enemy.draw()        
        
    player.update()
    player.draw()
        
        
        