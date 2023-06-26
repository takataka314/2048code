#!/usr/bin/env python
#coding: utf-8
from random import randint as rd
from itertools import product as pr
import pygame as pg
from pygame.locals import *
import sys

pg.init()
go = True
gc = True
score = 0
wk=800
fn="2048_数字.png"

sw,sh=(1920,1080)
sc=pg.display.set_mode((sw,sh),FULLSCREEN)
pg.display.set_caption(u"2048")

up,down,left,right=([0,-1],[0,1],[-1,0],[1,0])
sw,sh=(sc.get_width(),sc.get_height())
numl0=[[-1 for _ in range(4)] for _ in range(4)]

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

soh=pg.mixer.Sound("hit.wav")
sogo=pg.mixer.Sound("zannense.mp3")
sos=pg.mixer.Sound("決定、ボタン押下4.mp3")
ets = pg.mixer.Sound("キャンセル2.mp3")
cos = pg.mixer.Sound("coingame.mp3")
gtss = pg.mixer.Sound("決定、ボタン押下34.mp3")

def ltfc():
    for i,j in pr([0,1,2,3],[0,1,2,3]):
        gotf = False
        if i!=0:
            gotf = gotf or (numl0[i-1][j]==numl0[i][j])
            if gotf:
                return False
        if j!=0:
            gotf = gotf or (numl0[i][j-1]==numl0[i][j])
            if gotf:
                return False
        if j!=3:
            gotf = gotf or (numl0[i][j+1]==numl0[i][j])
            if gotf:
                return False
        if i!=3:
            gotf = gotf or (numl0[i+1][j]==numl0[i][j])
            if gotf:
                return False
    return True

def rds(stf,tf=False):
    global go
    if sum([r.count(-1) for r in numl0])>0:
        if tf:

            while True:
                x,y=(rd(0,3),rd(0,3))
                if numl0[x][y]==-1:
                    if rd(0,30)==0:
                        numl0[x][y]=1
                    else:
                        numl0[x][y]=0
                    if sum([r.count(-1) for r in numl0]) == 0 and ltfc():
                        go = False
                        break
                    if stf:
                        soh.play()
                    break
    else:
        if ltfc():
            go=False

def hm(dir):
    tf=False
    numl=[]
    ntf=[[True for _ in range(4)] for _ in range(4)]
    i0,j0=([0,1,2,3],[0,0,1,2,3])
    #上下
    if dir[0]==0:
        lr=dir[1]
        for i in range(4):
            nj=[]
            for j in range(4):
                nj+=[numl0[j][i]]
            numl+=[nj]
       #<->
    else:
        numl+=numl0
        lr=dir[0]
    ol=[(5+lr)//2,(1-lr)*5//2,-1*lr]
    j0=j0[ol[0]:ol[1]:ol[2]]
    
    for i,j in pr(i0,j0):
        if numl[i][j]!=-1:
            xs=numl[i][(j+1)*(lr+1)//2:((4-j)*lr+4+j)//2].count(-1)
            #一気に端に行く
            if j==(lr+1)*3//2-lr*xs:
                numl[i][(lr+1)*3//2]=numl[i][j]
                numl[i][j]=-1
                tf=True
            else:
                #一つ前と比較
                if numl[i][j+lr*(xs+1)]==numl[i][j]:
                    #計算前
                    if ntf[i][j+lr*(xs+1)]:
                        ntf[i][j+lr*(xs+1)]= not ntf[i][j+lr*(xs+1)]
                        numl[i][j+lr*(xs+1)]+=1
                        if numl[i][j+lr*(xs+1)] == 10:
                            global gc
                            gc = False
                        global score
                        score+=2**(numl[i][j+lr*(xs+1)]+1)
                        numl[i][j]=-1
                        tf=True
                    #計算後
                    else:
                        numl[i][j+lr*xs]=numl[i][j]
                        numl[i][j]=-1
                        tf=True
                #間があるとき
                elif xs!=0:
                    numl[i][j+lr*xs]=numl[i][j]
                    numl[i][j]=-1
                    tf=True
    numl2=[]
    if dir[0]==0:
        for i in range(4):
            nj=[]
            for j in range(4):
                nj+=[numl[j][i]]
            numl2+=[nj]
    else:
        numl2+=numl
    return (numl2,tf)

sf = pg.font.SysFont("hgep013", 80)
sf2 = pg.font.SysFont("hgep054", 200)#タイトル
sf3 = pg.font.SysFont("niskagnpultrabold",50)#操作説明
sf4 = pg.font.SysFont("arphicmarkertai4extrajis",80)#スペースキーでスタート
sf5 = pg.font.SysFont("NISSAIKOW8N",70)#HIGH SCORE
sf6_1 = pg.font.SysFont("hg創英ﾌﾟﾚｾﾞﾝｽeb",50)#説明内容
sf6_2 = pg.font.SysFont("hg創英ﾌﾟﾚｾﾞﾝｽeb",100)#残念．．．
sf7 = pg.font.SysFont("imprintshadow",80)#HIGH SCORE（数字）
sf8 = pg.font.SysFont("hgep030",150)#GAME OVER
sf9_1 = pg.font.SysFont("arphichanamojiume4ultrajis",100)#ハイスコア更新おめでとう！！
sf9_2 = pg.font.SysFont("arphichanamojiume4ultrajis",60)#ゲームクリア＆ハイスコア更新おめでとう！！
sf10 = pg.font.SysFont("script",200)#GAME CLEAR

with open("2048_説明.txt",encoding="utf-8") as stmi:
    sl = [x.split()[0] for x in stmi.readlines()]

def games():
    global numl0
    global score
    score=0
    numl0=[[-1 for _ in range(4)] for _ in range(4)]
    with open("score管理.txt",encoding="utf-8") as hs:
        scl = [int(i) for i in hs.readlines()]
        hsc = str(max(scl))

    stf=True
    pg.init()
    s2048=sf2.render("2048",True,(0,0,0),(238,138,248))
    ssousa=sf3.render("操作説明",True,(0,0,0))
    sstart = sf4.render("スペースキーでスタート",True,(0,0,0))
    shscore = sf5.render("HIGHSCORE",True,(31,141,166))
    shss = sf7.render(hsc,True,(0,0,0))
    sc.fill((136,196,70))
    for i in range(len(sl)):
        sstm=sf6_1.render(sl[i],True,(0,0,0))
        sc.blit(sstm,(0,500+ssousa.get_height()+sstm.get_height()*i))
    sc.blit(s2048,((sw-s2048.get_width())/2,30))
    sc.blit(ssousa,(0,500))
    sc.blit(sstart,((sw-sstart.get_width())/2,sh/2-50))
    sc.blit(shscore,((sw+s2048.get_width())/2+70,20))
    sc.blit(shss,(sw/2+s2048.get_width()/2+70+shscore.get_rect().centerx-shss.get_width()/2,20+shscore.get_height()))
    pg.display.update()
    while stf:
        for ev in pg.event.get():
            if ev.type == QUIT:
                sys.exit()
            if ev.type == KEYDOWN :
                if ev.key == K_SPACE:
                    sos.play()
                    stf = False
                if ev.key == K_ESCAPE:
                    sys.exit()
    pg.init()

def gameo():
    global go
    go = not go
    econg = False
    stf = True
    sogo.play()
    pg.time.wait(1000*2)
    with open("score管理.txt",encoding="utf-8") as hs:
        scl = [int(i) for i in hs.readlines()]
        hsc = max(scl)
        if hsc < score:
            econg = True
    with open("score管理.txt","a",encoding="utf-8") as hs:
        hs.write("\n"+str(score))
    pg.init()
    
    egameover = sf8.render("GAME OVER",True,(186,6,55))
    sc.fill((144,21,166))
    sc.blit(egameover,((sw-egameover.get_width())/2,20))
    
    if econg:
        eword = sf9_1.render("ハイスコア更新おめでとう！！",True,(0,0,0))
        eys = sf7.render("YOUR SCORE:"+str(score),True,(0,0,0))
        ehs = sf7.render("HIGH SCORE:"+str(score),True,(0,0,0))
        y = 20+egameover.get_height()
        sc.blit(eword,((sw-eword.get_width())/2,y))
        y += eword.get_height()
        sc.blit(eys,((sw-eys.get_width())/2,y))
        y += eys.get_height()
        sc.blit(ehs,((sw-ehs.get_width())/2,y))
    else:
        eword = sf6_2.render("残念．．．",True,(0,0,0))
        eys = sf7.render("YOUR SCORE:"+str(score),True,(0,0,0))
        ehs = sf7.render("HIGH SCORE:"+str(hsc),True,(0,0,0))
        y = 20+egameover.get_height()
        sc.blit(eword,((sw-eword.get_width())/2,y))
        y += eword.get_height()
        sc.blit(eys,((sw-eys.get_width())/2,y))
        y += eys.get_height()
        sc.blit(ehs,((sw-ehs.get_width())/2,y))
    y += ehs.get_height()+50
    estart = sf4.render("スペースキーでスタート画面へ",True,(0,0,0))
    sc.blit(estart,((sw-estart.get_width())/2,y))
    pg.display.update()
    while stf:
        for ev in pg.event.get():
            if ev.type == QUIT:
                sys.exit()
            if ev.type == KEYDOWN :
                if ev.key == K_SPACE:
                    ets.play()
                    stf = False
                if ev.key == K_ESCAPE:
                    sys.exit()

def gamec():
    cos.play()
    pg.init()
    pg.time.wait(1000*2)
    global gc
    gc = not gc
    ccong = False
    stf = True
    with open("score管理.txt",encoding="utf-8") as hs:
        scl = [int(i) for i in hs.readlines()]
        hsc = max(scl)
        if hsc < score:
            ccong = True
    with open("score管理.txt","a",encoding="utf-8") as hs:
        hs.write("\n"+str(score))
    cgameclear = sf10.render("GAME CLEAR",True,(0,0,0))
    sc.fill((209,222,60))
    sc.blit(cgameclear,((sw-cgameclear.get_width())/2,20))
    if ccong:
        cword = sf9_2.render("ゲームクリア＆ハイスコアおめでとう！！",True,(0,0,0))
        cys = sf7.render("YOUR SCORE:"+str(score),True,(0,0,0))
        chs = sf7.render("HIGH SCORE:"+str(score),True,(0,0,0))
        y = 20+cgameclear.get_height()
        sc.blit(cword,((sw-cword.get_width())/2,y))
        y += cword.get_height()
        sc.blit(cys,((sw-cys.get_width())/2,y))
        y += cys.get_height()
        sc.blit(chs,((sw-chs.get_width())/2,y))
    else:
        cword = sf9_2.render("ゲームクリアおめでとう！！",True,(0,0,0))
        cys = sf7.render("YOUR SCORE:"+str(score),True,(0,0,0))
        chs = sf7.render("HIGH SCORE:"+str(hsc),True,(0,0,0))
        y = 20+cgameclear.get_height()
        sc.blit(cword,((sw-cword.get_width())/2,y))
        y += cword.get_height()
        sc.blit(cys,((sw-cys.get_width())/2,y))
        y += cys.get_height()
        sc.blit(chs,((sw-chs.get_width())/2,y))
    y += chs.get_height()
    cstart = sf4.render("スペースキーでスタート画面へ",True,(0,0,0))
    sc.blit(cstart,((sw-cstart.get_width())/2,y+50))
    pg.display.update()
    while stf:
        
        for ev in pg.event.get():
            if ev.type == QUIT:
                sys.exit()
            if ev.type == KEYDOWN :
                if ev.key == K_SPACE:
                    ets.play()
                    stf = False
                if ev.key == K_ESCAPE:
                    sys.exit()

imgl=spi(li(fn))


while True:
    games()
    for _ in range(2):
        rds(False,True)
    sc.fill((56,34,45))
    pg.draw.rect(sc,(255,255,255),Rect((sw-wk)/2,(sh-wk)/2,wk,wk))
    for i in range(5):
        pg.draw.line(sc,(0,0,0),((sw-wk)/2,(sh-wk)/2+wk*i/4),((sw+wk)/2,(sh-wk)/2+wk*i/4),3)
        pg.draw.line(sc,(0,0,0),((sw-wk)/2+wk*i/4,(sh-wk)/2),((sw-wk)/2+wk*i/4,(sh+wk)/2),3)
    for i,j in pr([0,1,2,3],[0,1,2,3]):
                    nx=numl0[i][j]
                    if nx!=-1:
                        ix=(sw-wk)/2+wk/8-imgl[nx].get_width()/2+j*wk/4
                        iy=(sh-wk)/2+wk/8-imgl[nx].get_height()/2+i*wk/4
                        sc.blit(imgl[nx],(ix,iy))
    ptgts = sf6_1.render("終了は",True,(100,100,100))
    ptgts2 = sf6_1.render("escキー",True,(100,100,100))
    ptgts3 = sf6_1.render("左上にあります",True,(100,100,100))
    pts1 = sf7.render("SCORE",True,(255,255,255))
    pts2 = sf7.render(str(score),True,(255,255,255))
    sc.blit(pts1,(sw/2+wk/2,20))
    sc.blit(pts2,(sw/2+wk/2+pts1.get_rect().centerx-pts2.get_width()/2,20+pts1.get_height()))
    sc.blit(ptgts,(100,20))
    sc.blit(ptgts2,(100+ptgts.get_rect().centerx-ptgts2.get_width()/2,20+ptgts.get_height()))
    sc.blit(ptgts3,(100+ptgts.get_rect().centerx-ptgts3.get_width()/2,20+2*ptgts.get_height()))
    gts =True
    while go and gc and gts:
        pg.display.update()   
        for ev in pg.event.get():

            if ev.type==KEYDOWN:
                # print(score)
                tf=False
                
                if ev.key==K_ESCAPE:
                    gtss.play()
                    gts = False
                if ev.key==K_UP:
                    numl0,tf=hm(up)  
                if ev.key==K_DOWN:
                    numl0,tf=hm(down)
                if ev.key==K_LEFT:
                    numl0,tf=hm(left)
                if ev.key==K_RIGHT:
                    numl0,tf=hm(right)
                rds(True,tf)
                sc.fill((56,34,45))
                pg.draw.rect(sc,(255,255,255),Rect((sw-wk)/2,(sh-wk)/2,wk,wk))
                for i in range(5):
                    pg.draw.line(sc,(0,0,0),((sw-wk)/2,(sh-wk)/2+wk*i/4),((sw+wk)/2,(sh-wk)/2+wk*i/4),3)
                    pg.draw.line(sc,(0,0,0),((sw-wk)/2+wk*i/4,(sh-wk)/2),((sw-wk)/2+wk*i/4,(sh+wk)/2),3)
                for i,j in pr([0,1,2,3],[0,1,2,3]):
                    nx=numl0[i][j]
                    if nx!=-1:
                        ix=(sw-wk)/2+wk/8-imgl[nx].get_width()/2+j*wk/4
                        iy=(sh-wk)/2+wk/8-imgl[nx].get_height()/2+i*wk/4
                        sc.blit(imgl[nx],(ix,iy))
                pts2 = sf7.render(str(score),True,(255,255,255))
                sc.blit(pts1,(sw/2+wk/2,20))
                sc.blit(pts2,(sw/2+wk/2+pts1.get_rect().centerx-pts2.get_width()/2,20+pts1.get_height()))
                sc.blit(ptgts,(100,20))
                sc.blit(ptgts2,(100+ptgts.get_rect().centerx-ptgts2.get_width()/2,20+ptgts.get_height()))
                sc.blit(ptgts3,(100+ptgts.get_rect().centerx-ptgts3.get_width()/2,20+2*ptgts.get_height()))
                pg.display.update()
    if gts:
        if not gc:
            gamec()
        if not go:
            gameo()