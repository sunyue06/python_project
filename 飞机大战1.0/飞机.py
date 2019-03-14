import pygame
from plane_sprites import *
pygame.init()
#创建游戏口
screen=pygame.display.set_mode((512,768))
#绘制北京加载图像数据
bg=pygame.image.load('C:/Users/yue.sun/Desktop/自己/py/飞机大战1.0/素材/background.jpg')
#blit绘制，放在左上角原点
screen.blit(bg,(0,0))

#绘制英雄
hero=pygame.image.load('C:/Users/yue.sun/Desktop/自己/py/飞机大战1.0/素材/hero.png')
screen.blit(hero,(200,600))
#update更新屏幕显示,可以全做完之后统一执行update方法，调用一次就是一帧
pygame.display.update()

#创建游戏时钟
clock=pygame.time.Clock()
#定义rect记录飞机初始位置
hero_rect=pygame.Rect(200,600,120,79)

#创建敌机精灵
emeny=GameSprite('C:/Users/yue.sun/Desktop/自己/py/飞机大战1.0/素材/emeny.png')
#创建敌机精灵组
enemy_group=pygame.sprite.Group(emeny)

#游戏循环
while True:
    clock.tick(60)
    ##捕获事件
    #event_list=pygame.event.get()
    #if len(event_list)>0:
    #    print(event_list)
    #监听事件
    for even in pygame.event.get():
        #判断时间是否为退出事件
        if even.type==pygame.QUIT:
            print('游戏退出')
            pygame.quit()
            exit()

    #捕获飞机
    hero_rect.y -=1
    if hero_rect.y <= -79:
        hero_rect.y=768

    #只需要每次更新一下背景就会解决残影问题，把之前飞机影像遮挡了
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #让精灵组调用两个方法
    #update
    enemy_group.update()
    #draw在screen上显示
    enemy_group.draw(screen)




    pygame.display.update()
pygame.quit()#