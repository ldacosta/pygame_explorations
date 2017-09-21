#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.color import THECOLORS

from soccer.FontManager import cFontManager

class SoccerRegion:

    def __init__ (self, id, rect, soccer_field):

        self.id = id
        self.rect = rect
        self.soccer_field = soccer_field
        self.fontMgr = cFontManager(((None, 24), (None, 48), ('arial', 24)))

    def render (self):

        pygame.draw.rect(self.soccer_field.surface, THECOLORS['white'], self.rect, 1)
        self.fontMgr.Draw(self.soccer_field.surface, 'arial', 24, str(self.id), 
                          self.rect.center, THECOLORS['white'], 'center', 'center', True)
