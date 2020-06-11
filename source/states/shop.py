import pygame as pg
from .. import setup, tool
from .. import constants as c
from ..components import info
'''
#商店的内容
#除了在components.info中的背景设置(包括金币，游戏各类数据)，还需要表层的商品设计(读取图片+标题)
'''
class Shop(tool.State):
    def __init__(self):
        tool.State.__init__(self) #完成父类的初始化
    def startup(self, current_time, persist):
        self.next = c.SHOP #shop商店界面的下一级默认还是shop
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.Info(self.game_info, c.SHOP) #制作顶部信息

        self.setup_background()
        self.setup_goods()
        self.setup_cursor() #设置游标

    def setup_goods(self):
        #货架盈余总宽度453-210=243
        #货架盈余总高度 177
        #s商品y1 y2 货架底部y=100+279=379  下瓶底留6空 下瓶y=379-6-128=145 上瓶y=55=379/2-6-128
        # 商品x1 x2 空间三等分 空56 x1=56 x2=453-105-56=292
        image = tool.get_image(setup.GFX['shop_items'], 0, 0, 42, 51,
                                scale= c.SIZE_MULTIPLIER) #实际一件商品105*128
        rect = image.get_rect()
        rect.x, rect.y = (170+56, 100+55)
        self.image_dict['shop_item1'] = (image, rect)
        image = tool.get_image(setup.GFX['shop_items'], 42, 0, 42, 51,
                                scale= c.SIZE_MULTIPLIER) #实际一件商品105*128
        rect = image.get_rect()
        rect.x, rect.y = (170+56, 100+145)
        self.image_dict['shop_item2'] = (image, rect)
        image = tool.get_image(setup.GFX['shop_items3'], 84, 0, 42, 51,
                                scale= c.SIZE_MULTIPLIER) #实际一件商品105*128
        rect = image.get_rect()
        rect.x, rect.y = (170+292, 100+55)
        self.image_dict['shop_item3'] = (image, rect)
        image = tool.get_image(setup.GFX['shop_items'], 126, 0, 42, 50,
                                scale= c.SIZE_MULTIPLIER) #实际一件商品105*128
        rect = image.get_rect()
        rect.x, rect.y = (170+292, 100+145)
        self.image_dict['shop_item4'] = (image, rect)

    def setup_background(self):
        self.background = setup.GFX['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))
        #设置了背景（第一关的蓝天白云，如果后期切换关卡，应该切换到相应的关卡）
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.image_dict = {}
        image = tool.get_image(setup.GFX['shop_shelf2'], 0, 0, 151, 93,
                            scale= c.SIZE_MULTIPLIER*c.SIZE_MULTIPLIER_SHELF)#实际453*279
        rect = image.get_rect()
        rect.x, rect.y = (173, 100)#货架下边沿379 留有221
        self.image_dict['shop_shelf2'] = (image, rect)



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
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['shop_shelf2'][0],
                     self.image_dict['shop_shelf2'][1])
        surface.blit(self.image_dict['shop_item1'][0],
                     self.image_dict['shop_item1'][1])
        surface.blit(self.image_dict['shop_item2'][0],
                     self.image_dict['shop_item2'][1])
        surface.blit(self.image_dict['shop_item3'][0],
                     self.image_dict['shop_item3'][1])
        surface.blit(self.image_dict['shop_item4'][0],
                     self.image_dict['shop_item4'][1])
        #surface.blit(self.image_dict[''][0],
                   #  self.image_dict[''][1])
        surface.blit(self.cursor.image, self.cursor.rect)
        #self.overhead_info.draw(surface)
        self.overhead_info.testdraw(surface)
    def update_cursor(self, keys):
        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pg.K_DOWN]:
                self.cursor.state = c.SHOP
                self.player_index = 1
                self.game_info[c.PLAYER_NAME] = c.PLAYER_MARIO
        elif self.cursor.state == c.SHOP:
            self.cursor.rect.y = 403
            if keys[pg.K_UP]:
                self.cursor.state = c.PLAYER1
                self.player_index = 0
                self.game_info[c.PLAYER_NAME] = c.PLAYER_MARIO
        if keys[pg.K_RETURN]:
            self.reset_game_info()
            self.done = True

    def reset_game_info(self):
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_NUM] = 1

        self.persist = self.game_info
