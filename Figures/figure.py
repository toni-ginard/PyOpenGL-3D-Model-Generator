#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Random.Position import Position
from Random.Scale import Scale
from Random.Color import Color
from Random.Rotation import Rotation


class Figure:

    def __init__(self):
        self.posicio = []
        self.scale = []
        self.color = []
        self.graus_x = 0.0
        self.graus_y = 0.0

    def set_figure(self, posicio, scale, color, graus_x, graus_y):
        self.posicio = posicio
        self.scale = scale
        self.color = color
        self.graus_x = graus_x
        self.graus_y = graus_y

    def set_random_figure(self):
        self.posicio = Position.get_random_position()
        self.scale = Scale.get_random_scale()
        self.color = Color.get_random_color()
        self.graus_x = Rotation.get_random_rotation()
        self.graus_y = Rotation.get_random_rotation()

    @staticmethod
    def get_random_atrib_figures(nfigures):
        figures = []
        for i in range(nfigures):
            figure = Figure()
            figure.set_random_figure()
            figures.append(figure)

        return figures
