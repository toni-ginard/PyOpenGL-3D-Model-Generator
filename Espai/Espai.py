#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
from OpenGL.GL import *
import math


class Espai:

    @staticmethod
    def view():
        return pyrr.matrix44.create_look_at(pyrr.Vector3([0.0, 0.0, 5.0]),  # eye
                                            pyrr.Vector3([0.0, 0.0, 0.0]),  # target
                                            pyrr.Vector3([0.0, 1.0, 0.0]))  # up

    @staticmethod
    def proj(dist, width, height, front_pane, back_pane):
        return pyrr.matrix44.create_perspective_projection_matrix(dist, width / height, front_pane, back_pane)

    @staticmethod
    def scale(shader, mida):
        scale = pyrr.matrix44.create_from_scale(pyrr.Vector3(mida), dtype=float)
        scale_loc = glGetUniformLocation(shader, "scale")
        glUniformMatrix4fv(scale_loc, 1, GL_FALSE, scale)

    # definir world space de la figura
    @staticmethod
    def model(shader, posicio):
        model = pyrr.matrix44.create_from_translation(posicio)
        model_loc = glGetUniformLocation(shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    @staticmethod
    def transf(shader, graus):
        transf = pyrr.matrix44.create_from_y_rotation(math.radians(graus))
        transf_loc = glGetUniformLocation(shader, "transf")
        glUniformMatrix4fv(transf_loc, 1, GL_FALSE, transf)

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
    def dibuixar_figura(vao, shader, indexs_figura):
        glBindVertexArray(vao)
        glUseProgram(shader)
        glDrawElements(GL_TRIANGLES, indexs_figura.size, GL_UNSIGNED_INT, None)
        glUseProgram(0)
        glBindVertexArray(0)

    @staticmethod
    def definir_figura(shader, view, proj, figura):
        glUseProgram(shader)
        Espai.view_loc(shader, view)
        Espai.proj_loc(shader, proj)
        Espai.scale(shader, figura.scale)
        Espai.model(shader, figura.posicio)
        Espai.set_color(shader, figura.color)
        glUseProgram(0)
