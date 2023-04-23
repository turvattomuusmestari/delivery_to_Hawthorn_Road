import pygame as pg

class Settings:
    resolution = [1280, 720]
    resratio = resolution[0] / resolution[1]
    fps = 60
    def toggle_mouse_visibility():
        pg.mouse.set_visible(not pg.mouse.get_visible())