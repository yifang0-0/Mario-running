import pygame
from pygame.examples.scrap_clipboard import screen

pygame.init()

w,h=500,500
pygame.display.set_model((w,h))
screen=pygame.display.get_surface()

bgpic=pygame.display.load("level_1.png")
bgpic=pygame.transform.scale(bgpic,(w,h))
mario_image=pygame.image.load("mario.png")

mario = pygame.sprite.Sprite()
mario.image=mario_image
mario.rect=mario.image.get_rec()
mario.x,mario_image.y=w/3,h/2

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
    screen.bilt(bgpic,(0,0))
    player_group.draw(screen)
    pygame.display.update()
