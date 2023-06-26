#cording:utf-8-
from random import randint as rd
import pygame as pg
from pygame.locals import *
import sys

pg.init()
wk=800
fn="2048_数字.png"
sw,sh=(1920,1080)
sc=pg.display.set_mode((sw,sh),FULLSCREEN)
sf = pg.font.SysFont("hgep013", 80)
sf2 = pg.font.SysFont("hgep054", 80)
ss=sf.render(str(123),True,(0,0,0),(255,255,255))

def li(fn,ck=None):
    try:
        img=pg.image.load(fn)
    except pg.error:
        raise SystemExit
    img=img.convert()
    if ck is not None:
        if ck is -1:
            ck=img.get_at((0,0))
    return img
    
def spi(img):
    imgl=[]
    for i in range(0,1925,175):
        suf=pg.Surface((175,175))
        suf.blit(img,(0,0),(i,0,175,175))
        suf.convert()
        imgl+=[suf]
    return imgl


numl=[[-1 for _ in range(4)] for _ in range(4)]
print(numl)

# sw,sh=(sc.get_width(),sc.get_height())
clock = pg.time.Clock()
fr=0
t=0
while True:
    # sc.fill((180,215,100))
    # sc.blit(ss,(100,200))
    # pg.draw.rect(sc,(255,255,255),Rect((sw-wk)/2,(sh-wk)/2,wk,wk))
    # for i in range(5):
    #     pg.draw.line(sc,(0,0,0),((sw-wk)/2,(sh-wk)/2+wk*i/4),((sw+wk)/2,(sh-wk)/2+wk*i/4),3)
    #     pg.draw.line(sc,(0,0,0),((sw-wk)/2+wk*i/4,(sh-wk)/2),((sw-wk)/2+wk*i/4,(sh+wk)/2),3)
    pg.display.update()
    for ev in pg.event.get():
        if ev.type==KEYDOWN and ev.key == K_ESCAPE:sys.exit()

