import pygame as pg
import os


def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pg.Surface([width, height])
    rect = image.get_rect()
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pg.transform.scale(image, (int(rect.width*scale), int(rect.height*scale)))
    return image


def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def load_all_sound(directory, accept=('.mp3')):
    sounds = {}
    for sound in os.listdir(directory):
        name, ext = os.path.splitext(sound)
        if ext.lower() in accept:
            sound_path = os.path.join(directory, sound)
            sounds[name] = sound_path
    return sounds
