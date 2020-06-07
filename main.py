#游戏主要入口
import pygame

from source import tools,setup
from source.states import main_menu, load_screen, level, shop

def main():
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level(),
        'shop':shop.Shop()
    }
    game = tools.Game(state_dict, 'shop')
    game.run()

if __name__ == "__main__":
    main()