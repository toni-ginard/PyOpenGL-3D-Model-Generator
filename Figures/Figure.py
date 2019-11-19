#!/usr/bin/env python
# -*- coding: utf-8 -*-


import Figures.Buffer as Buffer
import Random.Position as Position
import Random.Scale as Scale
import Random.Color as Color
import Random.Rotation as Rotation
from Space.Space import *


class Figure:

    vertices = []
    indexes = []
    scale = []
    x_axis = 0.0
    y_axis = 0.0
    position = []
    color = []

    def __init__(self, vertices=None, indexes=None, scale=None, x_axis=0.0, y_axis=0.0, position=None, color=None):
        self.vertices = vertices
        self.indexes = indexes
        self.scale = scale
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.position = position
        self.color = color

    def set_buffer(self, shader, offset):
        """ Set buffer attributes for a figure.

        :param shader: figure's shader object.
        :param offset: offset for normal vector.
        """
        Buffer.bind_vbo(self.vertices)
        Buffer.bind_ebo(self.indexes)
        Buffer.get_attribute_location(shader, "position")
        Buffer.vertex_attribute(6, 0, 0)
        Buffer.get_attribute_location(shader, "aNormal")
        Buffer.vertex_attribute(6, offset, 1)

    def draw(self, shader, view, figure, vao):
        """ Draws a figure.

        :param shader: figure's shader object.
        :param numpy.array view: camera coordinates.
        :param figure: object to set attributes and to draw.
        :param vao: vertex array object.
        """
        set_figure_attribute_matrices(shader, view, figure)
        draw_figure(shader, self.indexes, vao)

    def set_figure_random(self):
        """ Set random attributes (scaling, rotation, position, color) for a figure.

        :return: figure with attributes on random values.
        """
        self.scale = Scale.get_random_scale()
        self.x_axis = Rotation.get_random_rotation()
        self.y_axis = Rotation.get_random_rotation()
        self.position = Position.get_random_position()
        self.color = Color.get_random_color()

    @staticmethod
    def get_random_figures(num_figures):
        """ Returns a number of figures, determined by the parameter num_figures, which attributes (position,
        scaling, color and axis rotation) are set randomly.

        :param num_figures: number of random figures that sets.
        :rtype numpy.array
        :return: array of figures.
        """
        figures = []
        for i in range(num_figures):
            figure = Figure()
            figure.set_figure_random()
            figures.append(figure)

        return figures
