#游戏主控
#控制屏幕帧率
import pygame
import random
import os
#from . import main_manu
class Game:
    def __init__(self):
        #设置游戏界面大小
        self.screen=pygame.display.get_surface()
        self.clock=pygame.time.Clock()

    def run(self,state):
        path=os.getcwd()
        GRAPHICS=load_pic(path)
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            state.update(self.screen)

            pygame.display.update()
            self.clock.tick(48)

def load_pic(path,accept=('.jpg','.png','.gif')):
    i_picture={}
    for pic in os.listdir(path):
        name,ext=os.path.splitext(pic)
        if ext.lower()in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img=img.convert_alpha()#alpha说明图片带有透明层，在此处转换可以加快渲染速度
            else:
                img=img.convert()
            i_picture[name]=img
    return i_picture

def get_partofpic(sheet,x,y,width,height,colorkey,scale):
    image=pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(colorkey)#抠图底色
    image=pygame.transform.scale(image,((int(width*scale)),(int(scale*height))))#scale放大倍数,第二个参数需要做成数组
    return image