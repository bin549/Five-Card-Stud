import os
import pygame as pg
from . import constants as c
from . import tools


""" Game Info"""
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

""" Resource Loading """
# Sprite
CharacterGFX = tools.load_all_gfx(os.path.join("resources", "sprites", "Characters"))
EnvGFX = tools.load_all_gfx(os.path.join("resources", "sprites", "Environments"))
UIGFX = tools.load_all_gfx(os.path.join("resources", "sprites", "UI"))
CardGFX = tools.load_all_gfx(os.path.join("resources", "sprites", "Cards"))
# Sounds
Musics = tools.load_all_sound(os.path.join("resources", "Sounds", "Musics"))
Ambients = tools.load_all_sound(os.path.join("resources", "Sounds", "Ambients"))
Effects = tools.load_all_sound(os.path.join("resources", "Sounds", "Effects"))
