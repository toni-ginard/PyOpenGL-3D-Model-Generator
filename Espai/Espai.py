#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
from OpenGL.GL import *
import math

class Espai:

    @staticmethod
    def view(eye, target):
        return pyrr.matrix44.create_look_at(pyrr.Vector3(eye),
                                            pyrr.Vector3(target),
                                            pyrr.Vector3([0.0, 1.0, 0.0]))

    @staticmethod
    def proj(dist, width, height, front_pane, back_pane):
        return pyrr.matrix44.create_perspective_projection_matrix(dist, width / height, front_pane, back_pane)

    @staticmethod
    def set_scale(shader, mida):
        scale = pyrr.matrix44.create_from_scale(pyrr.Vector3(mida), dtype=float)
        scale_loc = glGetUniformLocation(shader, "scale")
        glUniformMatrix4fv(scale_loc, 1, GL_FALSE, scale)

    # definir world space de la figura
    @staticmethod
    def set_model(shader, posicio):
        model = pyrr.matrix44.create_from_translation(posicio)
        model_loc = glGetUniformLocation(shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    @staticmethod
    def set_rot_x(shader, graus):
        rot = pyrr.matrix44.create_from_x_rotation(math.radians(graus))
        rot_loc = glGetUniformLocation(shader, "rot_x")
        glUniformMatrix4fv(rot_loc, 1, GL_FALSE, rot)

    @staticmethod
    def set_rot_y(shader, graus):
        rot = pyrr.matrix44.create_from_y_rotation(math.radians(graus))
        rot_loc = glGetUniformLocation(shader, "rot_y")
        glUniformMatrix4fv(rot_loc, 1, GL_FALSE, rot)

    @staticmethod
    def set_color(shader, color):
        my_color = pyrr.vector3.create(color[0], color[1], color[2], dtype=float)
        color_loc = glGetUniformLocation(shader, "myColor")
        glUniform3fv(color_loc, 1, my_color)

    @staticmethod
    def view_loc(shader, view):
        view_loc = glGetUniformLocation(shader, "view")
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    @staticmethod
    def proj_loc(shader, proj):
        proj_loc = glGetUniformLocation(shader, "proj")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)

    @staticmethod
    def dibuixar_figura(vao, shader, indexs_figure):
        glBindVertexArray(vao)
        glUseProgram(shader)
        glDrawElements(GL_TRIANGLES, indexs_figure.size, GL_UNSIGNED_INT, None)
        glUseProgram(0)
        glBindVertexArray(0)

    @staticmethod
    def definir_figura(shader, view, proj, figure):
        glUseProgram(shader)
        Espai.view_loc(shader, view)
        Espai.proj_loc(shader, proj)
        Espai.set_scale(shader, figure.scale)
        Espai.set_rot_x(shader, figure.graus_x)
        Espai.set_rot_y(shader, figure.graus_y)
        Espai.set_model(shader, figure.posicio)
        Espai.set_color(shader, figure.color)
        glUseProgram(0)
