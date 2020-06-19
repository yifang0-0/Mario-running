import pygame

from ..import setup,tool
from ..components import mydatabase as db
from ..components import dataBaseGlobalData as GD

import pygame as pg
from .. import tool
from .. import setup
from .. import constants as c
from .. components import info

class Menu(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        persist = {c.COIN_TOTAL: GD.shopinfo[c.COINID],
                   c.SCORE: 0,
                   c.LIVES: GD.shopinfo[c.LIFEID],
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_NUM: 1,
                   c.PLAYER_NAME: c.PLAYER_MARIO,
                   c.MAX_LEVEL:1,
                   c.SUCCESSED:0,
                   c.STARTUP:1
                   }#这里是初始化的persist,但是之后每一次应该从数据库中读取
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        self.next = c.LOAD_SCREEN #设置下一个状态
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.Info(self.game_info, c.MAIN_MENU,self.persist)
        self.canUse=0
        self.lastKeyEvent=pg.key.get_pressed()
        self.setup_background()
        self.setup_cursor()
        if self.persist[c.STARTUP]==0:
            self.reset_game_info()
        else:
            self.initial_game_info()
            self.setup_player()

    def setup_background(self):
        if self.persist[c.LEVEL_NUM]==1:
            self.background = setup.GFX['level_1']
        if self.persist[c.LEVEL_NUM]==2:
            self.background = setup.GFX['level_2']
        if self.persist[c.LEVEL_NUM]==3:
            self.background = setup.GFX['level_3']
        if self.persist[c.LEVEL_NUM]==4:
            self.background = setup.GFX['level_4']

        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.image_dict = {}
        image = tool.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
                            (255, 0, 220), c.SIZE_MULTIPLIER)
        rect = image.get_rect()
        rect.x, rect.y = (170, 100)
        self.image_dict['GAME_NAME_BOX'] = (image, rect)


    def setup_player(self):
        self.player_list = []
        player_rect_info = [(178, 32, 12, 16), (178, 128, 12, 16)]
        for rect in player_rect_info:
            image = tool.get_image(setup.GFX['mario_bros'],
                                *rect, c.BLACK, 2.9)
            rect = image.get_rect()
            rect.x, rect.bottom = 110, c.GROUND_HEIGHT
            self.player_list.append((image, rect))
        self.player_index = 0

    def setup_cursor(self):
        self.cursor = pg.sprite.Sprite()
        self.cursor.image = tool.get_image(setup.GFX[c.ITEM_SHEET], 24, 160, 8, 8, c.BLACK, 3)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 358)
        self.cursor.rect = rect
        self.cursor.state = c.PLAYER1

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.player_image = self.player_list[self.player_index][0]
        self.player_rect = self.player_list[self.player_index][1]
        temp=pg.key.get_pressed()
        if self.lastKeyEvent!=temp:
            self.lastKeyEvent=temp
            self.canUse=1
        if self.canUse:
            self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_NAME_BOX'][0],
                     self.image_dict['GAME_NAME_BOX'][1])
        surface.blit(self.player_image, self.player_rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)
    def update_cursor(self, keys):
        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pg.K_DOWN]:
                self.cursor.state = c.SHOP
                self.next = c.SHOP
                self.player_index = 0
                self.game_info[c.PLAYER_NAME] = c.PLAYER_MARIO
                self.canUse=0
        elif self.cursor.state == c.SHOP:
            self.cursor.rect.y = 403
            if keys[pg.K_UP]:
                self.next = c.LOAD_SCREEN
                self.cursor.state = c.PLAYER1
                self.player_index = 0
                self.game_info[c.PLAYER_NAME] = c.PLAYER_MARIO
                self.canUse=0
        if keys[pg.K_RETURN]:
            self.reset_game_info()
            self.done = True

    '''
            if keys[pg.K_ENTER]:
                #self.reset_game_info()
                self.done = True
    File "F:\大三下课程\软件工程\Mario-running\Mario-running\source\states\main_manu.py", line 99, in update_cursor
        if keys[pg.K_ENTER]:
    AttributeError: module 'pygame' has no attribute 'K_ENTER'
    '''
    def reset_game_info(self):
        self.game_info[c.LIVES] = GD.shopinfo[c.LIFEID]
        self.game_info[c.CURRENT_TIME] = 0.0
        self.persist = self.game_info
    def initial_game_info(self):
        self.game_info[c.COIN_TOTAL] = GD.shopinfo[c.COINID]
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = GD.shopinfo[c.LIFEID]
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_NUM] = 1
        self.persist = self.game_info