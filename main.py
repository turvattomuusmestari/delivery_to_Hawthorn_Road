from game import Game
from dialogues import *
#levels#
from level_main_menu import MainMenu
from level_road_1 import Level1

if __name__ == "__main__":
    Game.levels["main menu"] = MainMenu
    Game.levels["level 1"] = Level1
    MainMenu.start()
    while True:
        Time.tick()
        Input.update()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                Game.exit_game()
            if e.type == pg.KEYDOWN:
                    if e.key == 32:
                        Settings.toggle_mouse_visibility()
                    elif e.key == pg.K_z:
                        Input.keys_down["Z"] = 1
                    elif e.key == pg.K_x:
                        Input.keys_down["X"] = 1
                    elif e.key == pg.K_c:
                        Input.keys_down["C"] = 1
                    elif e.key == pg.K_LEFT:
                        Input.keys_down["A"] = 1
                    elif e.key == pg.K_UP:
                        Input.keys_down["W"] = 1
                    elif e.key == pg.K_DOWN:
                        Input.keys_down["S"] = 1
                    elif e.key == pg.K_RIGHT:
                        Input.keys_down["D"] = 1
        Game.update()
        Window.update()