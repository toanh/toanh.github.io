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
        
        self.images = []
        self.images.append("https://i.imgur.com/LFQBqx9.png")
        self.images.append("https://i.imgur.com/dE9HwPZ.png")
        
        self.width = 103
        self.height = 52
        
        self.anim_time = 20
        self.anim_timer = self.anim_time
        
        self.fires = 0

    def update(self):
        self.anim_timer -= 1
        if self.anim_timer < 0:
            self.anim_timer = self.anim_time
            
        self.cool_down_timer -= 1
        if self.cool_down_timer < 0:
            self.cool_down_timer = 0
            
        if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
            self.x -= self.speed
        if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
            self.x += self.speed
        if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
            self.y += self.speed
        if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
            self.y -= self.speed
        
        if ((graphics.isKeyPressed(KEY_J)  or graphics.isKeyPressed(KEY_V_FIRE))) and self.cool_down_timer == 0:
            
            newBullet = Bullet()
            newBullet.x = self.x + (self.width - newBullet.width) / 2
            newBullet.y = self.y + self.height - newBullet.height
            bullets.append(newBullet)
            self.cool_down_timer = self.cool_down
            
    def draw(self):
        graphics.drawImage(self.images[self.anim_timer // (self.anim_time / len(self.images)) - 1], self.x, self.y)             
            

class Bullet (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 1
        self.g = 0
        self.b = 0      
        
        self.speed = 10
        
        self.width = 8
        self.height = 8
        
        self.image = "https://i.imgur.com/DxrwkDN.png"
        
    def update(self):
        if self.state == 0:
            self.y += self.speed
        elif self.state == 1:
            self.r -= 0.2
            if self.r <= 0:
                self.b = 0
                self.state = 2
            
    def draw(self):
        graphics.drawImage(self.image, self.x, self.y)             
            
 
class Enemy (Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.r = 0
        self.g = 0
        self.b = 1      
        
        self.speed = -2
        
        self.width = 32
        self.height = 32
        
        self.state = 0
        
        self.anim_time = 16
        self.anim_timer = 0
        
        self.asteroids = []
        self.asteroids.append(["https://i.imgur.com/k0qlX2L.png", 42, 21])
        self.asteroids.append(["https://i.imgur.com/UfQzcaA.png", 81, 73])
        self.asteroids.append(["https://i.imgur.com/Tsf4FTm.png", 53, 57])

        
        choice = random.randint(0, len(self.asteroids) - 1)
        self.image = self.asteroids[choice][0]
        self.width = self.asteroids[choice][1]
        self.height = self.asteroids[choice][2]
        
        self.explosion_images = []
        self.explosion_images.append("https://i.imgur.com/HCrQpQy.png")
        self.explosion_images.append("https://i.imgur.com/71LFhqC.png")        
        self.explosion_images.append("https://i.imgur.com/DHQDg12.png")  
        self.explosion_images.append("https://i.imgur.com/ioYnFKv.png")  
        self.explosion_images.append("https://i.imgur.com/1JZwyhq.png")          
        

    def update(self):
        if self.state == 0:
            self.y += self.speed
        elif self.state == 1:
            self.anim_timer += 1
            if self.anim_timer >= self.anim_time:
                self.anim_timer = 0
                self.state = 2

    def draw(self):
        if self.state == 0:
            graphics.drawImage(self.image, self.x, self.y)
        elif self.state == 1:
            graphics.drawImage(self.explosion_images[(self.anim_timer) // (self.anim_time / len(self.explosion_images))], self.x, self.y)                     
         

player = Player()
bullets = []
enemies = []
spawnTime = 50
spawnTimer = spawnTime

graphics.playSound("sounds/Eliminator_intro.mp3")

@loop_animation
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
    
    
    