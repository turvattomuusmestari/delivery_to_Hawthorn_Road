from settings import *

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