#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Random.Position import Position
from Random.Scale import Scale
from Random.Color import Color
from Random.Rotation import Rotation


class Figure:

    def __init__(self):
        self.position = []
        self.scale = []
        self.color = []
        self.x_axis = 0.0
        self.y_axis = 0.0

    def set_figure(self, position, scale, color, x_axis, y_axis):
        """ Set attribute values.

        :param position: coordinates in world space.
        :param numpy.array scale: scaling factor.
        :param numpy.array color: rgb color.
        :param float x_axis: x axis rotation.
        :param float y_axis: y axis rotation.
        """
        self.position = position
        self.scale = scale
        self.color = color
        self.x_axis = x_axis
        self.y_axis = y_axis

    def set_random_figure(self):
        """ Set random attributes (position, scaling, color, rotation) for a figure.

        :return: figure with attributes on random values.
        """
        self.position = Position.get_random_position()
        self.scale = Scale.get_random_scale()
        self.color = Color.get_random_color()
        self.x_axis = Rotation.get_random_rotation()
        self.y_axis = Rotation.get_random_rotation()

    @staticmethod
    def get_random_figures(nfigures):
        """ Returns a number of figures, determined by the parameter nfigures, which attributes are
        set randomly.

        :param nfigures: number of random figures that sets.
        :return: numpy.array of figures.
        """
        figures = []
        for i in range(nfigures):
            figure = Figure()
            figure.set_random_figure()
            figures.append(figure)

        return figures
