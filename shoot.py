import app
from pygame import *
from random import *
window = display.set_mode((900, 600))
display.set_caption('-_-')

background = image.load('galaxy.jpg')
background = transform.scale(background, (900, 600))

clock = time.Clock()
FPS = 120  # )))))))

mixer.init()

mixer.music.play()

lost = 0
score = 0



class GameSprite(sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, speed, width, height):
        super().__init__()
        self.img = transform.scale(image.load(img), (60, 60))
        self.rect = self.img.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed

    def draw(self):
        window.blit(self.img, self.rect)


class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if pressed[K_d] and self.rect.x < 900:
            self.rect.x += self.speed
        if pressed[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
        if pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

    def fire(self):
        pass


class Enemy(GameSprite):

    def update(self):
        self.rect.y += 600
        global lost
        if self.rect.y >= 600:
            self.rect.x = randint(0, 900-80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()





player = Player('rocket.png', 50, 500, 10, 60, 100)

enemies = sprite.Group()
for i in range(7):
    enemy = Enemy('ufo.png', randint(0, 900 - 80), 0, randint(1, 5), 80, 40)
    enemies.add(enemy)
Bullet = sprite.Group()


game = True
finish = False


while game:
    window.blit(background, (0, 0))
    player.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)

app.exec_
