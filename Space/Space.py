#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
import math
from OpenGL.GL import *
from Figures.Projection import Projection
from Figures.View import View


def set_view_matrix(shader, view):
    """ Set camera position defining eye and target position (direction).

    :param shader: figure shader object.
    :param view: camera view.
    """
    view = View(view[0], view[1])
    view.set_view(shader)


def set_projection_matrix(shader):
    """ Set perspective projection matrix. """
    projection = Projection()
    projection.set_projection(shader)


def set_scale_matrix(shader, scale_factor):
    """ Set scale matrix to apply to a figure.

    :param shader: figure shader object.
    :param numpy.array scale_factor: transformation matrix to apply to the figure.
    """
    scale = pyrr.matrix44.create_from_scale(pyrr.Vector3(scale_factor), dtype=float)
    scale_loc = glGetUniformLocation(shader, "scale")
    glUniformMatrix4fv(scale_loc, 1, GL_FALSE, scale)


def set_rot_x_matrix(shader, degrees):
    """ Set figures' X axis rotation.

    :param shader: figure shader object.
    :param float degrees: figure's X axis rotation degrees.
    """
    rotation = pyrr.matrix44.create_from_x_rotation(math.radians(degrees))
    rotation_loc = glGetUniformLocation(shader, "rot_x")
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)


def set_rot_y_matrix(shader, degrees):
    """ Set figures' Y axis rotation.

    :param shader: figure shader object.
    :param float degrees: figure's Y axis rotation degrees.
    """
    rotation = pyrr.matrix44.create_from_y_rotation(math.radians(degrees))
    rotation_loc = glGetUniformLocation(shader, "rot_y")
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)


def set_model_matrix(shader, position):
    """ Set figure's world space coordinates.

    :param shader: figure shader object.
    :param numpy.array position: world coordinates.
    """
    model = pyrr.matrix44.create_from_translation(position)
    model_loc = glGetUniformLocation(shader, "model")
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)


def set_color_vector(shader, color):
    """ Set figure's color.

    :param shader: figure shader object.
    :param numpy.array color: rgb color.
    """
    my_color = pyrr.vector3.create(color[0], color[1], color[2], dtype=float)
    color_loc = glGetUniformLocation(shader, "myColor")
    glUniform3fv(color_loc, 1, my_color)


def set_light_matrix(shader):
    """ Set figure's light effect.

    :param shader: figure shader object.
    """
    light = pyrr.matrix44.create_from_translation(pyrr.Vector3([1.2, 1.0, 2.0]))
    light_loc = glGetUniformLocation(shader, "light")
    glUniformMatrix4fv(light_loc, 1, GL_FALSE, light)


def set_figure_attribute_matrices(shader, view, figure):
    """ Sets all the attributes of a figure inside the screen space,
    as well as its view and projection matrices. Prepares the figure to be drawn.

    :param shader: figure shader object.
    :param view: view matrix (camera position).
    :param figure: object containing the figure's attributes.
    """
    glUseProgram(shader)
    set_view_matrix(shader, view)
    set_projection_matrix(shader)
    set_scale_matrix(shader, figure.scale)
    set_rot_x_matrix(shader, figure.x_axis)
    set_rot_y_matrix(shader, figure.y_axis)
    set_model_matrix(shader, figure.position)
    set_color_vector(shader, figure.color)
    set_light_matrix(shader)
    glUseProgram(0)


def draw_figure(shader, figure_indexes, vao):
    """ Draws a figure from its shader object, the coordinates of its vertices
    and its vao.

    :param shader: figure shader object.
    :param figure_indexes: figure's indexes coordinates.
    :param vao: figure's vertex buffer object.
    """
    glBindVertexArray(vao)
    glUseProgram(shader)
    glDrawArrays(GL_TRIANGLES, 0, figure_indexes.size)
    # glDrawElements(GL_TRIANGLES, figure_indexes.size, GL_UNSIGNED_INT, None)
    glUseProgram(0)
    glBindVertexArray(0)

