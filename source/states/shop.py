import pygame as pg
from .. components import info
from .. import tools, setup
from .. import constants as c

class Shop:
    def __init__(self):
        self.finished = False
        self.startup()
        self.setup_shopitems()
        self.info = info.Info('shop')

    def startup(self):
        self.background = setup.GRAPHICS['shopBackground']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, (int(self.background_rect.width * c.BG_MULTI),
                                                                   int(self.background_rect.height * c.BG_MULTI)))
        self.viewport = setup.SCREEN.get_rect()

    def setup_shopitems(self):
        self.item1 = pg.sprite.Sprite()
        self.item1.image = tools.get_image(setup.GRAPHICS['shop_items'], 1, 1, 230, 225, (255, 255, 255), 1)
        rect = self.item1.image.get_rect()
        rect.x, rect.y = (50, 50)
        self.item1.rect = rect

        self.item2 = pg.sprite.Sprite()
        self.item2.image = tools.get_image(setup.GRAPHICS['shop_items'], 231, 1, 230, 225, (255, 255, 255), 1)
        rect = self.item2.image.get_rect()
        rect.x, rect.y = (280, 50)
        self.item2.rect = rect

        self.item3 = pg.sprite.Sprite()
        self.item3.image = tools.get_image(setup.GRAPHICS['shop_items'], 461, 1, 230, 225, (255, 255, 255), 1)
        rect = self.item3.image.get_rect()
        rect.x, rect.y = (510, 50)
        self.item3.rect = rect

        self.item4 = pg.sprite.Sprite()
        self.item4.image = tools.get_image(setup.GRAPHICS['shop_items'], 1, 226, 230, 225, (255, 255, 255), 1)
        rect = self.item4.image.get_rect()
        rect.x, rect.y = (50, 275)
        self.item4.rect = rect

        self.item5 = pg.sprite.Sprite()
        self.item5.image = tools.get_image(setup.GRAPHICS['shop_items'], 231, 226, 230, 225, (255, 255, 255), 1)
        rect = self.item5.image.get_rect()
        rect.x, rect.y = (280, 275)
        self.item5.rect = rect

        self.item6 = pg.sprite.Sprite()
        self.item6.image = tools.get_image(setup.GRAPHICS['shop_items'], 461, 226, 230, 225, (255, 255, 255), 1)
        rect = self.item6.image.get_rect()
        rect.x, rect.y = (510, 275)
        self.item6.rect = rect

    def update(self, surface, keys):
        surface.blit(self.background, self.viewport)
        pg.draw.rect(surface, (0, 197, 205), (50, 50, 690, 450), 0)
        pg.draw.rect(surface, (0, 255, 205), (50, 500, 690, 50), 0)

        surface.blit(self.item1.image, self.item1.rect)
        surface.blit(self.item2.image, self.item2.rect)
        surface.blit(self.item3.image, self.item3.rect)
        surface.blit(self.item4.image, self.item4.rect)
        surface.blit(self.item5.image, self.item5.rect)
        surface.blit(self.item6.image, self.item6.rect)
