from gizmos import *

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