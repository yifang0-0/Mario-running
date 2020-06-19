#游戏主控
#控制屏幕帧率
import pygame as pg
import random
import os
from abc import ABC, abstractmethod
#from . import main_manu

keybinding = {
    'action':pg.K_s,
    'jump':pg.K_SPACE,
    'left':pg.K_LEFT,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN,
    'esc':pg.K_ESCAPE
}
# class Game:
#     def __init__(self):
#         #设置游戏界面大小
#         self.screen=pygame.display.get_surface()
#         self.clock=pygame.time.Clock()
#
#     def run(self,state):
#         path=os.getcwd()
#         GRAPHICS=load_pic(path)
#         while True:
#             for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                     pygame.display.quit()
#                     quit()
#                 elif event.type == pygame.KEYDOWN:
#                     self.keys = pygame.key.get_pressed()
#                 elif event.type == pygame.KEYUP:
#                     self.keys = pygame.key.get_pressed()
#             state.update(self.screen)
#
#             pygame.display.update()
#             self.clock.tick(48)
#
# def load_pic(path,accept=('.jpg','.png','.gif')):
#     i_picture={}
#     for pic in os.listdir(path):
#         name,ext=os.path.splitext(pic)
#         if ext.lower()in accept:
#             img = pygame.image.load(os.path.join(path,pic))
#             if img.get_alpha():
#                 img=img.convert_alpha()#alpha说明图片带有透明层，在此处转换可以加快渲染速度
#             else:
#                 img=img.convert()
#             i_picture[name]=img
#     return i_picture
#
# def get_partofpic(sheet,x,y,width,height,colorkey,scale):
#     image=pygame.Surface((width,height))
#     image.blit(sheet,(0,0),(x,y,width,height))
#     image.set_colorkey(colorkey)#抠图底色
#     image=pygame.transform.scale(image,((int(width*scale)),(int(scale*height))))#scale放大倍数,第二个参数需要做成数组
#     return image
# __author__ = 'marble_xu'
#
# import os
# import pygame as pg
# from abc import ABC, abstractmethod


class State():
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.next = None
        self.persist = {}

    @abstractmethod
    def startup(self, current_time, persist):
        '''abstract method'''

    def cleanup(self):
        self.done = False
        return self.persist

    @abstractmethod
    def update(sefl, surface, keys, current_time):
        '''abstract method'''

class Control():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            # elif event.type == pg.KEYLEFT:
            #     self.keys = pg.key.get_pressed()
            # elif event.type == pg.KEYRIGHT:
            #     self.keys = pg.key.get_pressed()
            # elif event.type == pg.KEYESCAPE:
            #     self.keys = pg.key.get_pressed()
                #hhhhh闹笑话了呀 这里检测的是键盘的动作而不是具体按了哪个键

    def main(self):
        while not self.done:
            self.event_loop() #获取键盘动作
            self.update() #按照子类的方法具体实现更新
            pg.display.update() #pg.display.update()实现了更新的真正实施
            self.clock.tick(self.fps) #self.clock.tick(double n)表示了每秒循环n次 用来调整while循环的速度 此处ftp设置为60，每秒刷新屏幕60次

def get_image(sheet, x, y, width, height, colorkey, scale):
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(colorkey)
        image = pg.transform.scale(image,
                                   (int(rect.width*scale),
                                    int(rect.height*scale)))
        return image

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics
