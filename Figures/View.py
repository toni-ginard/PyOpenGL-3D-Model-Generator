#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyrr
from OpenGL.GL import *


class View:

    eye = []
    target = []

    def __init__(self, eye, target):
        """ Instantiates view matrix attributes. """
        self.eye = eye
        self.target = target

    def set_view(self, shader):
        """ Return view matrix. """
        view = pyrr.matrix44.create_look_at(pyrr.Vector3(self.eye),
                                            pyrr.Vector3(self.target),
                                            pyrr.Vector3([0.0, 1.0, 0.0]))
        view_loc = glGetUniformLocation(shader, "view")
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
