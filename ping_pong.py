from pygame import * 

clock = time.Clock() 
FPS = 60 
win_width = 600 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
display.set_caption('Пинг понг') 
background = transform.scale(image.load('back.png'),(600, 500)) 

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
       sprite.Sprite.__init__(self) 
 
 
       self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
       self.speed = player_speed 
 
 
       self.rect = self.image.get_rect() 
       self.rect.x = player_x 
       self.rect.y = player_y 
    def reset(self): 
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite): 
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -70: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 270: 
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > -70: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 270: 
            self.rect.y += self.speed 

tr1 = Player('tennrack.png', 10, 100, 25, 300, 10) 
tr2 = Player('tennrack.png', 555, 100, 25, 300, 10) 
ball = GameSprite('ball.png', 275, 250, 75, 75, 5)

font.init()
font1 = font.SysFont('Arial', 35)
font2 = font.SysFont('Arial', 35)
lose1 = font1.render(
    'PLAYER 1 LOSE', True, (255, 0, 0)
)
lose2 = font2.render(
    'PLAYER 2 LOSE', True, (255, 0, 0)
)


speed_x = 5
speed_y = 5

finish = False 
run = True  
while run: 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
    if finish != True:
        window.blit(background,(0,0)) 
        tr1.update_1()
        tr1.reset()
        tr2.update_2()
        tr2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 425 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(tr1, ball) or sprite.collide_rect(tr2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x  > 525:
        finish = True
        window.blit(lose2, (200, 200))
    display.update() 
    time.delay(50)
