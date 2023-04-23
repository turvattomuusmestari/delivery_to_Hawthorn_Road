from game import Game
from gizmos import *
from dialogues import *
from pathlib import Path

class Lang:
    rus = {}
    eng = {}
    #--------------#
    tag = ""
    eng[tag] = ""
    rus[tag] = ""
    #--------------#
    dictionary = {"english" : eng, "russian" : rus}
    def get(tag):
        return Lang.dictionary[Settings.language][tag]

class Level1:    
    def start():
        Game.Level = Level1
        Game.Menu = None
    def draw():
        Window.canvas.fill([5,220,220])
    def update():
        pass