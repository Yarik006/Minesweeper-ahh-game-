import pygame as pg
from random import*

WIDTH=700
HEIGHT=600

WINDOW=pg.display.set_mode((WIDTH, HEIGHT))

WHITE=(255, 255, 255)

WINDOW.fill(WHITE)


class GameSprite:
   def __init__(self,image,x,y,width,height,iw,ih):
       self.image=pg.transform.scale(self.image.load(image),(iw,ih))
       self.rect=pg.Rect(x,y,width,height)
   def update(self):
       WINDOW.blit(self.image,(self.rect.x,self.rect.y))

clock = pg.time.Clock()

run=True

while run: 


class Character(GameSprite):
    def move(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y-=5
        if keys[pg.K_DOWN]:
            self.rect.y+=5
        if keys[pg]
            pass




    for e in pg.event.get():
        if e.type==pg.QUIT:
            run=False

    pg.display.update()
    clock.tick(60)