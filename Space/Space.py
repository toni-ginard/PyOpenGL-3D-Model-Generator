#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pyrr
import math
from OpenGL.GL import *


def set_view(eye, target):
    """ Set camera position defining eye and target position (direction).

    :param numpy.array eye: camera position in world coordinates.
    :param numpy.array target: target position in world coordinates.
    :rtype: numpy.array
    :return: matrix that can be used as View Matrix.
    """
    return pyrr.matrix44.create_look_at(pyrr.Vector3(eye),
                                        pyrr.Vector3(target),
                                        pyrr.Vector3([0.0, 1.0, 0.0]))


def set_projection(degrees, aspect_ratio, front_pane, back_pane):
    """ Set perspective projection matrix.

    :param float degrees: field of view in y direction in degrees.
    :param float aspect_ratio: aspect ratio of the view (width / height).
    :param float front_pane: distance from the viewer to the near plane.
    :param float back_pane: distance from the viewer to the far plane.
    :rtype: numpy.array
    :return: projection matrix representing the specified perspective.
    """
    return pyrr.matrix44.create_perspective_projection_matrix(degrees, aspect_ratio, front_pane, back_pane)


def set_scale(shader, size):
    """ Set scale matrix to apply to a figure.

    :param shader: figure shader object.
    :param numpy.array size: transformation matrix to apply to the figure.
    """
    scale = pyrr.matrix44.create_from_scale(pyrr.Vector3(size), dtype=float)
    scale_loc = glGetUniformLocation(shader, "scale")
    glUniformMatrix4fv(scale_loc, 1, GL_FALSE, scale)


def set_model(shader, position):
    """ Set figure's world space coordinates.

    :param shader: figure shader object.
    :param numpy.array position: world coordinates.
    """
    model = pyrr.matrix44.create_from_translation(position)
    model_loc = glGetUniformLocation(shader, "model")
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)


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


def projection_loc(shader, proj):
    proj_loc = glGetUniformLocation(shader, "proj")
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)


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


def set_figure_attributes(shader, view, projection, figure):
    """
    Sets all the attributes of a figure inside the screen space,
    as well as its view and projection matrices. Prepares the figure to be drawn.

    :param shader: figure shader object.
    :param view: view matrix (camera position).
    :param projection: projection matrix.
    :param figure: object containing the figure's attributes.
    """
    glUseProgram(shader)
    view_loc(shader, view)
    projection_loc(shader, projection)
    set_scale(shader, figure.scale)
    set_rot_x(shader, figure.x_axis)
    set_rot_y(shader, figure.y_axis)
    set_model(shader, figure.position)
    set_color(shader, figure.color)
    set_light(shader)
    glUseProgram(0)
