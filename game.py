import sys
import pygame as pg

class Game:
    Level = None
    Menu = None
    levels = {}
    def new_game():
        pass
    def update():
        if not Game.Menu == None:
            Game.Menu.update()
        elif not Game.Level == None:
            Game.Level.update()
        else:
            pass
        if not Game.Level == None:
            Game.Level.draw()
    def exit_game():
        pg.quit()
        sys.exit()