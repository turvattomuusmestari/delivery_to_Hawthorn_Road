from game import Game
from gizmos import *
from dialogues import *
from pathlib import Path

class Lang:
    rus = {}
    eng = {}

    tag = "ng"
    eng[tag] = "new game"
    rus[tag] = "новая игра"
    #
    tag = "lg"
    eng[tag] = "load game"
    rus[tag] = "загрузить"
    #
    tag = "exit"
    eng[tag] = "exit"
    rus[tag] = "выход"
    #
    tag = "title"
    eng[tag] = "Delivery to Hawthorn Road"
    rus[tag] = "Доставка на Хосон Роуд"
    #
    dictionary = {"english" : eng, "russian" : rus}
    def get(tag):
        return Lang.dictionary[Settings.language][tag]

class MainMenu:    
    options = []
    options.append(Option(lambda: Game.levels["level 1"].start(), text = Lang.get("ng")))
    options.append(Option(lambda: print(open("save.fun").read()), text = Lang.get("lg")))
    options[-1].locked = not Path("save.fun").exists()
    options.append(Option(Game.exit_game, text = Lang.get("exit")))
    menu = Option_box(options, pos = [510, 350], fontname = "default_font_big", mode = "center", delta = 14)
    menu.previous = menu
    title = Text.render_text("default_font_giant", Lang.get("title"))
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