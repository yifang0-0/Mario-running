import pygame
from pygame.examples.scrap_clipboard import screen

pygame.init()

w,h=900,250
pygame.display.set_mode((w,h))
screen=pygame.display.get_surface()#获取画布

bgpic=pygame.image.load("level_1.png")
#bgpic=pygame.transform.scale(bgpic,(w,h))#载入底图
mario_image=pygame.image.load("mario.png")#载入马里奥

mario = pygame.sprite.Sprite()
mario.image=mario_image
mario.rect=mario.image.get_rect()#获得马里奥的长宽高等信息
mario.rect.x,mario.rect.y=w/2,h/2

player_group = pygame.sprite.Group()
player_group.add(mario)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y+=10
            if keys[pygame.K_UP]:
                mario.rect.y-=10
            if keys[pygame.K_LEFT]:
                mario.rect.x-=10
            if keys[pygame.K_RIGHT]:
                mario.rect.x+=10
    screen.blit(bgpic,(0,0))
    player_group.draw(screen)
    pygame.display.update()
