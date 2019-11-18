#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
from OpenGL.GL import *


class Projection:

    degrees = 0.0
    aspect_ratio = 0.0
    front_pane = 0.0
    back_pane = 0.0

    def __init__(self):
        """ Instantiates projection matrix attributes. """
        self.degrees = 60.0
        self.aspect_ratio = 1.0
        self.front_pane = 0.1
        self.back_pane = 100.0

    def set_projection(self, shader):
        """ Return projection matrix. """
        projection = pyrr.matrix44.create_perspective_projection_matrix(self.degrees,
                                                                        self.aspect_ratio,
                                                                        self.front_pane,
                                                                        self.back_pane)
        proj_loc = glGetUniformLocation(shader, "proj")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
