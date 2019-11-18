#!/usr/bin/env python
# -*- coding: utf-8 -*-


from OpenGL.GL import *


def bind_vao():
    """ Bind vertex array object
    :return: vertex array object.
    """
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    return vao


def bind_vbo(vertices):
    """ Bind vertex buffer object.
    Copy buffer's figure to memory.
    """
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)  # link 2 buffers
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)


def bind_ebo(indexes):
    """ Bind element buffer object.
    Copy indexes' buffer to memory.
    """
    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indexes.nbytes, indexes, GL_STATIC_DRAW)


def get_attribute_location(shader, attribute):
    """ Get attribute location """
    return glGetAttribLocation(shader, attribute)


def vertex_attribute(nvertices, offset, param):
    """
    :param nvertices: number of vertices to draw.
    :param offset: offset to place on vertices position.
    :param param: param to enable its attribute.
    """
    glVertexAttribPointer(param, 3, GL_FLOAT, GL_FALSE, nvertices * 4, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(param)  # 1 vertex == 3 coordinates, float = 12 bytes
    # 0 o atribut ("position")    # si tenim normals, 1 vèrtex = 6 coordenades = 24 byte