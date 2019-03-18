#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
from OpenGL.GL import *


class Espai:

    @staticmethod
    def view(x, y, z):
        return pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z]))

    @staticmethod
    def proj(dist, width, height, front_pane, back_pane):
        return pyrr.matrix44.create_perspective_projection_matrix(dist, width / height, front_pane, back_pane)

    @staticmethod
    def view_proj(shader, view, proj):
        Espai.view_loc(shader, view)
        Espai.proj_loc(shader, proj)

    # definir la posició espacial de la figura
    @staticmethod
    def model(posicio):
        return pyrr.matrix44.create_from_translation(posicio)

    @staticmethod
    def view_loc(shader, view):
        view_loc = glGetUniformLocation(shader, "view")
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    @staticmethod
    def proj_loc(shader, proj):
        proj_loc = glGetUniformLocation(shader, "proj")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)

    @staticmethod
    def model_loc(shader, model):
        model_loc = glGetUniformLocation(shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)