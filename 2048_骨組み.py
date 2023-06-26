from random import randint as rd
import pygame as pg
from pygame.locals import *
import sys


pg.init()
sw,sh=(200,200)
sc=pg.display.set_mode((sw,sh))
pg.display.set_caption(u"2048")
up,down,left,right=([0,-1],[0,1],[-1,0],[1,0])
numl=[[-1 for _ in range(4)] for _ in range(4)]
def rds():
    while True:
        x,y=(rd(0,3),rd(0,3))
        if numl[x][y]==-1:
            if rd(0,9)==0:
                numl[x][y]=1
            else:
                numl[x][y]=0
            break
# ↑

def hm(dir):
    numl2=[]
    if dir[0]==0:
        for i in range(4):
            numl2+=[r[i] for r in numl]
    else:
        numl2=numl
    
    for i in range(4):
        for j in range(4):
            i2=(1-dir[0])*3//2+dir[0]*i
            j2=(1-dir[0])*3//2+dir[0]*j

            if numl2[i2][j2]!=-1 and j2!=(dir[0]+1)*3//2:
                if dir[0]<0:
                    xs=numl2[i2][:j2].count(-1)
                else:
                    xs=numl2[i2][(3-j2):].count(-1)
                if xs==0:
                    if numl2[i2][j2]==numl2[i2][j2+dir[0]]:
                        numl2[i2][j2+dir[0]]+=1
                        numl2[i2][j2]=-1
                elif xs==j2:
                    numl2[i2][(dir[0]+1)*3//2]+=1
                    numl2[i2][j2]=-1
                else:
                    xs+=1
                    if numl2[i2][j2]==numl2[i2][j2+xs*dir[0]]:
                        numl2[i2][j2+xs*dir[0]]+=1
                    elif numl2[i2][j2+xs*dir[0]]==-1:
                        numl2[i2][j2+xs*dir[0]]=numl2[i2][j2]
                    else:
                        numl2[i2][j2+(xs-1)*dir[0]]=numl2[i2][j2]
                    numl2[i2][j2]=-1
    return numl2



for _ in range(2):
    rds()

while True:
    sc.fill((56,34,45))
    pg.display.update()
    for ev in pg.event.get():
        if ev.type==KEYDOWN:
            if ev.key==K_ESCAPE:
                sys.exit()
            if ev.key==K_UP:
                numl2=hm(up)  
                print("u")              
            if ev.key==K_DOWN:
                print("d")
                numl2=hm(down)
            if ev.key==K_LEFT:
                print("l")
                numl2=hm(left)
            if ev.key==K_RIGHT:
                print("r")
                numl2=hm(right)
            rds()
            print(numl2)
    