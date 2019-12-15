#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Figures.Figure import Figure
from Random.Color import *


class Background:

    back = Figure()
    bottom = Figure()
    left = Figure()
    right = Figure()

    def __init__(self, back=Figure(), bottom=Figure(), left=Figure(), right=Figure()):
        self.back = back
        self.bottom = bottom
        self.left = left
        self.right = right

    def set_background(self):
        """ Sets a static background. """
        x_rand = random.uniform(-2, 2)
        y_rand = random.uniform(-2, 1)
        background_color = get_background_color()

        self.back = Figure(scale=[16.0, 18.0, 10.0],
                           x_axis=0,
                           y_axis=0,
                           position=[-1.0 + x_rand, 3.0 + y_rand, -10.0],
                           color=background_color)
        self.bottom = Figure(scale=[16.0, 18.0, 10.0],
                             x_axis=90,
                             y_axis=0,
                             position=[-1.0 + x_rand, -5.0 + y_rand, -10.0],
                             color=background_color)
        self.left = Figure(scale=[16.0, 18.0, 10.0],
                           x_axis=0,
                           y_axis=90,
                           position=[-7.0 + x_rand, 3.0 + y_rand, -10.0],
                           color=background_color)
        self.right = Figure(scale=[16.0, 18.0, 10.0],
                            x_axis=0,
                            y_axis=90,
                            position=[7.0 + x_rand, 3.0 + y_rand, -10.0],
                            color=background_color)

    def draw_background(self, plane, shader, view, vao):
        """ Draws the background for the scene, representing room's walls.

        :param plane: object to draw the planes.
        :param shader: figure's shader object.
        :param view: camera.
        :param vao: vertex array object.
        """
        plane.draw(shader, view, self.back, vao)
        plane.draw(shader, view, self.bottom, vao)
        plane.draw(shader, view, self.left, vao)
        plane.draw(shader, view, self.right, vao)
