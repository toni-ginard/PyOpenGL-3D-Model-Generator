#!/usr/bin/env python
# -*- coding: utf-8 -*-


import Space.Space as Space
import Random.Position as Position
import Random.Scale as Scale
import Random.Color as Color
import Random.Rotation as Rotation
import Figures.Buffer as Buffer


class Figure:

    def __init__(self):
        self.vertices = []
        self.indexes = []
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

    def set_figure_random(self):
        """ Set random attributes (position, scaling, color, rotation) for a figure.

        :return: figure with attributes on random values.
        """
        self.position = Position.get_random_position()
        self.scale = Scale.get_random_scale()
        self.color = Color.get_random_color()
        self.x_axis = Rotation.get_random_rotation()
        self.y_axis = Rotation.get_random_rotation()

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

    def draw(self, shader, view, projection, figure, vao):
        """ Draws a figure.

        :param shader: figure's shader object.
        :param numpy.array view: camera coordinates.
        :param numpy.array projection: perspective projection matrix.
        :param figure: object to set attributes and to draw.
        :param vao: vertex array object.
        """
        Space.set_figure_attributes(shader, view, projection, figure)
        Space.draw_figure(shader, self.indexes, vao)

    """ ************************************************************************************************************ """

    @staticmethod
    def get_random_figures(nfigures):
        """ Returns a number of figures, determined by the parameter nfigures, which attributes (position,
        scaling, color and axis rotation) are set randomly.

        :param nfigures: number of random figures that sets.
        :rtype numpy.array
        :return: array of figures.
        """
        figures = []
        for i in range(nfigures):
            figure = Figure()
            figure.set_figure_random()
            figures.append(figure)

        return figures
