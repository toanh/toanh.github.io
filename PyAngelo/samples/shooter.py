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
        
        self.state = 0          # 0 = alive, 1 = dying, 2 = dead
        
    def draw(self):
        graphics.drawRect(self.x, self.y, self.x + self.width, self.y + self.height, \
                            self.r, self.g, self.b, self.a)    
        
class Player (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 0
        self.g = 1
        self.b = 0
        
        self.speed = 2
        
        self.cool_down = 10
        self.cool_down_timer = self.cool_down

    def update(self):
        self.cool_down_timer -= 1
        if self.cool_down_timer < 0:
            self.cool_down_timer = self.cool_down
            
        if graphics.isKeyPressed(KEY_A):
            self.x -= self.speed
        if graphics.isKeyPressed(KEY_D):
            self.x += self.speed
        if graphics.isKeyPressed(KEY_W):
            self.y += self.speed
        if graphics.isKeyPressed(KEY_S):
            self.y -= self.speed
            
        if graphics.isKeyPressed(KEY_J) and self.cool_down_timer == self.cool_down:
            newBullet = Bullet()
            newBullet.x = self.x + (self.width - newBullet.width) / 2
            newBullet.y = self.y + self.height - newBullet.height
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
        if self.state == 0:
            self.y += self.speed
        elif self.state == 1:
            self.r -= 0.2
            if self.r <= 0:
                self.b = 0
                self.state = 2
            self.width += 8
            self.x -= 4
        
     
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
        if self.state == 0:
            self.y += self.speed
        elif self.state == 1:
            self.b -= 0.2
            if self.b <= 0:
                self.b = 0
                self.state = 2
         

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
        if bullet.y > graphics.height or bullet.state == 2:
            bullets.remove(bullet)

    for enemy in enemies:
        if enemy.y < -enemy.height or enemy.state == 2:
            enemies.remove(enemy)    

    b = 0
    while b < len(bullets):
        bullet = bullets[b]
        e = 0
        while e < len(enemies):
            enemy = enemies[e]

            if enemy.state == 0 and graphics.overlaps(bullet.x, bullet.y, bullet.width, bullet.height, enemy.x, enemy.y, enemy.width, enemy.height):
                # collision!
                enemy.state = 1
                bullet.state = 1
            e += 1
        b += 1

    e = 0
    while e < len(enemies):
        enemy = enemies[e]
        if enemy.state == 0 and graphics.overlaps(player.x, player.y, player.width, player.height, enemy.x, enemy.y, enemy.width, enemy.height):
            # collision!
            enemy.state = 1
        e += 1
            


        
    for enemy in enemies:
        enemy.update()
        enemy.draw()      
        
    for bullet in bullets:
        bullet.update()
        bullet.draw()        
        
    player.update()
    player.draw()
        
        
        