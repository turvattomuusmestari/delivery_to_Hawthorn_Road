from game import Game
from gizmos import *
from dialogues import *
from pathlib import Path

class MainMenu:
    options = []
    options.append(Option(None, text = "new game"))
    options.append(Option(lambda: print(open("save.fun").read()), text = "load game"))
    options[-1].locked = not Path("save.fun").exists()
    options.append(Option(Game.exit_game, text = "exit"))
    menu = Option_box(options, pos = [510, 350], fontname = "default_font_big", mode = "center", delta = 14)
    menu.previous = menu
    title = Text.render_text("default_font_giant", "Delivery to Hawthorn Road")
    #title = Text.render_text("default_font_giant", "Доставка на Хафсорн Роад")
    def start():
        Game.Level = MainMenu
        Game.Menu = MainMenu.menu
    def draw():
        Window.canvas.fill([255,0,0])  
        Window.canvas.blit(MainMenu.title,[200, 200])
        pg.draw.circle(Window.canvas,[0,0,0],[0,0],50)
        pg.draw.circle(Window.canvas,[0,0,0],[Settings.resolution[0],0],50)
        pg.draw.circle(Window.canvas,[0,0,0],[0,Settings.resolution[1]],50)
        pg.draw.circle(Window.canvas,[0,0,0],[Settings.resolution[0],Settings.resolution[1]],50)
        MainMenu.menu.draw()
    def update():
        pass