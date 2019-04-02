#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Random.Position import Position
from Random.Scale import Scale
from Random.Color import Color


class Figura:

    def __init__(self):
        self.posicio = []
        self.scale = []
        self.color = []

    def set_figura(self, posicio, scale, color):
        self.posicio = posicio
        self.scale = scale
        self.color = color

    def set_posicio(self):
        self.posicio = Position.get_random_position()

    def set_scale(self):
        self.scale = Scale.get_random_scale()

    def set_color(self):
        self.color = Color.get_random_color()

    @staticmethod
    def get_figures(nfigures):
        figures = []
        for i in range(nfigures):
            figura = Figura()
            figura.set_figura(Position.get_random_position(), Scale.get_random_scale(), Color.get_random_color())
            figures.append(figura)

        return figures
