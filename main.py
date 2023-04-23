import sys
import pygame as pg
from pathlib import Path

class Settings:
    resolution = [1280, 720]
    resratio = resolution[0] / resolution[1]
    fps = 60
    def toggle_mouse_visibility():
        pg.mouse.set_visible(not pg.mouse.get_visible())

class Window:
    window = pg.display.set_mode(Settings.resolution, pg.RESIZABLE)
    canvas = pg.Surface(Settings.resolution)
    ui_canvas = pg.Surface(Settings.resolution, pg.SRCALPHA)
    #pg.display.set_icon("")
    pg.display.set_caption("Delivery to Hawthorn Road")
    pg.mouse.set_visible(0)
    ##
    def update():
        Window.canvas.blit(Window.ui_canvas,[0,0])
        Window.ui_canvas.fill([0,0,0,0])
        Window.window.fill([0,0,0])
        info = pg.display.Info()
        dx,dy = [0,0]
        if info.current_w/info.current_h < Settings.resratio:
            w = info.current_w
            h = w/Settings.resratio
            dy = (info.current_h - h)/2
        else:
            h = info.current_h
            w = h*Settings.resratio
            dx = (info.current_w - w)/2
        Window.window.blit(pg.transform.scale(Window.canvas, [w, h]), [dx,dy])
        pg.display.update()

class Text:
    pg.font.init()
    fonts = {"default_font_small" : pg.font.Font(None, 14),
        "default_font" : pg.font.Font(None, 36),
        "default_font_big" : pg.font.Font(None, 64),
        "default_font_large" : pg.font.Font(None, 86),
        "default_font_giant" : pg.font.Font(None, 100)
        }
    def render_text(font_name, text, color = [0,0,0]):
        return Text.fonts[font_name].render(text, False, color)

class Input:
    keys_down = {"Z" : 0, "X" : 0, "C" : 0, "A" : 0, "W" : 0, "S" : 0, "D" : 0}
    keys = {"A" : 0, "W" : 0, "S" : 0, "D" : 0}
    def update():
        pressed = pg.key.get_pressed()
        Input.keys_down = {"Z" : 0, "X" : 0, "C" : 0, "A" : 0, "W" : 0, "S" : 0, "D" : 0}
        Input.keys = {"A" : pressed[pg.K_LEFT], "W" : pressed[pg.K_UP], "S" : pressed[pg.K_DOWN], "D" : pressed[pg.K_RIGHT]}

class Time:
    clock = pg.time.Clock()
    delta_time = 0
    def tick():
        Time.delta_time = 1/Time.clock.tick(Settings.fps)

###
class Game:
    Level = None
    Menu = None
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
###

class Option:
    def __init__ (self, foo, text = "option", comment = ""):
        self.foo = foo
        self.text = text
        self.comment = comment
        self.locked = False

class Option_box:
    def __init__(self, options, linewidth = 1, pos = [0, 0], mode = 'normal', delta = 0, title = "", fontname = "default_font", titlefontname = "default_font_big", colorA = (255,0,0), colorB = (0, 0, 0), colorC = (255, 255, 255)):
        self.visible = True
        self.previous = None
        self.index = 0
        self.options = options
        self.options_text = {}
        self.options_highlighted_text = {}
        if mode in ["inverse", "normal", "center"]:
            self.mode = mode
        else:
            self.mode = "normal"
        w_arr = []
        h_arr = []
        self.linewidth = linewidth
        if len(title) > 0:
            self.title_text = Text.render_text(titlefontname, title, colorA)
            rect = self.title_text.get_rect()
            w_arr.append(rect.width)
            self.delta0 = rect.height + self.linewidth
        else:
            self.title_text = None
            self.delta0 = 0
        for o in options:
            self.options_text[o] = Text.render_text(fontname, o.text, colorA)
            self.options_highlighted_text[o] = Text.render_text(fontname, o.text, colorC)
            rect = self.options_text[o].get_rect()
            w_arr.append(rect.width)
            h_arr.append(rect.height)
            print(o.text)
        self.delta = max(h_arr) + delta
        self.rect = [pos[0], pos[1], max(w_arr), self.delta0 + delta*(len(options)-1)+max(h_arr)*len(options)]
        self.fontname =  fontname 
        self.colorA =  colorA   
        self.colorB =  colorB   
        self.colorC =  colorC
    def draw(self):
        if not self.visible:
            return
        i = 0
        x, y, w, h = self.rect
        pg.draw.rect(Window.ui_canvas, self.colorB, [x-0.1*w, y-0.1*h, w*1.2, h*1.2])
        if not self.title_text == None:
            Window.ui_canvas.blit(self.title_text, [x, y])
            line_y = y + self.delta0 - self.linewidth/2
            pg.draw.line(Window.ui_canvas, self.colorA, [x, line_y], [x + w, line_y], self.linewidth)
        for o in self.options:
            ox = x
            a = self.options_highlighted_text[o]
            b = self.options_text[o]
            if self.mode == "center":
                ox = x + w/2 - self.options_text[o].get_rect().width/2
            elif self.mode == "inverse":
                ox = x + w - self.options_text[o].get_rect().width
            if self.options[self.index] == o:
                a.set_alpha(255 - o.locked*100)
                Window.ui_canvas.blit(a, [ox, y+i*self.delta + self.delta0])
            else:
                b.set_alpha(255 - o.locked*100)
                Window.ui_canvas.blit(b, [ox, y+i*self.delta + self.delta0])
            i += 1
    def update(self):
        if Input.keys_down['Z']:
            if not self.options[self.index].foo == None:
                if self.options[self.index].locked:
                    return
                self.options[self.index].foo()
            return
        if Input.keys_down['X']:
            if self.previous == self:
                return
            Game.Menu = self.previous
            self.visible = False
            return
        self.index += Input.keys_down['S'] - Input.keys_down['W']
        if self.index < 0:
            self.index = len(self.options) - 1
        elif self.index > len(self.options) - 1:
            self.index = 0

class MainMenu:
    options = []
    options.append(Option(None, text = "new game"))
    options.append(Option(lambda: print(open("save.fun").read()), text = "load game"))
    options[-1].locked = not Path("save.fun").exists()
    options.append(Option(Game.exit_game, text = "exit"))
    menu = Option_box(options, pos = [510, 350], fontname = "default_font_big", mode = "center", delta = 14)
    menu.previous = menu
    title = Text.render_text("default_font_giant", "Delivery to Hawthorn Road")
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
        
if __name__ == "__main__":
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