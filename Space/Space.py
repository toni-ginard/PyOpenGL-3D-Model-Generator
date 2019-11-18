#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
import math
from OpenGL.GL import *


def set_view(shader, view):
    """ Set camera position defining eye and target position (direction).

    :param shader: figure shader object.
    :param view: camera view.
    """
    view = pyrr.matrix44.create_look_at(pyrr.Vector3(view[0]),
                                        pyrr.Vector3(view[1]),
                                        pyrr.Vector3([0.0, 1.0, 0.0]))
    view_loc = glGetUniformLocation(shader, "view")
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)


def set_projection(shader):
    """ Set perspective projection matrix. """
    projection = pyrr.matrix44.create_perspective_projection_matrix(60.0, 1, 0.1, 100.0)
    proj_loc = glGetUniformLocation(shader, "proj")
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


def set_scale(shader, size):
    """ Set scale matrix to apply to a figure.

    :param shader: figure shader object.
    :param numpy.array size: transformation matrix to apply to the figure.
    """
    scale = pyrr.matrix44.create_from_scale(pyrr.Vector3(size), dtype=float)
    scale_loc = glGetUniformLocation(shader, "scale")
    glUniformMatrix4fv(scale_loc, 1, GL_FALSE, scale)


def set_rot_x(shader, degrees):
    """ Set figures' X axis rotation.

    :param shader: figure shader object.
    :param float degrees: figure's X axis rotation degrees.
    """
    rotation = pyrr.matrix44.create_from_x_rotation(math.radians(degrees))
    rotation_loc = glGetUniformLocation(shader, "rot_x")
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)


def set_rot_y(shader, degrees):
    """ Set figures' Y axis rotation.

    :param shader: figure shader object.
    :param float degrees: figure's Y axis rotation degrees.
    """
    rotation = pyrr.matrix44.create_from_y_rotation(math.radians(degrees))
    rotation_loc = glGetUniformLocation(shader, "rot_y")
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)


def set_model(shader, position):
    """ Set figure's world space coordinates.

    :param shader: figure shader object.
    :param numpy.array position: world coordinates.
    """
    model = pyrr.matrix44.create_from_translation(position)
    model_loc = glGetUniformLocation(shader, "model")
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)


def set_color(shader, color):
    """ Set figure's color.

    :param shader: figure shader object.
    :param numpy.array color: rgb color.
    """
    my_color = pyrr.vector3.create(color[0], color[1], color[2], dtype=float)
    color_loc = glGetUniformLocation(shader, "myColor")
    glUniform3fv(color_loc, 1, my_color)


def set_light(shader):
    """ Set figure's light effect.

    :param shader: figure shader object.
    """
    light = pyrr.matrix44.create_from_translation(pyrr.Vector3([1.2, 1.0, 2.0]))
    light_loc = glGetUniformLocation(shader, "light")
    glUniformMatrix4fv(light_loc, 1, GL_FALSE, light)


def view_loc(shader, view):
    view_loc = glGetUniformLocation(shader, "view")
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)


def draw_figure(shader, figure_indexes, vao):
    """
    Draws a figure from its shader object, the coordinates of its vertices
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


def set_figure_attributes(shader, view, figure):
    """
    Sets all the attributes of a figure inside the screen space,
    as well as its view and projection matrices. Prepares the figure to be drawn.

    :param shader: figure shader object.
    :param view: view matrix (camera position).
    :param figure: object containing the figure's attributes.
    """
    glUseProgram(shader)
    set_view(shader, view)
    set_projection(shader)
    set_scale(shader, figure.scale)
    set_rot_x(shader, figure.x_axis)
    set_rot_y(shader, figure.y_axis)
    set_model(shader, figure.position)
    set_color(shader, figure.color)
    set_light(shader)
    glUseProgram(0)
