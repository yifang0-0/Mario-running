#游戏入口
import pygame
from source import tool ,setup
from source.states import main_manu,load_screen, level
from source import constants as c

import pygame as pg

if __name__=='__main__':
    game = tool.Control()
    state_dict = {c.MAIN_MENU: main_manu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()
    pg.quit()

