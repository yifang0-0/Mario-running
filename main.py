#游戏入口
import pygame
from source import tool ,setup,main_manu

def main():
    game=tool.Game()
    state=main_manu()
    game.run(state)

if __name__=="__main__":
    main()