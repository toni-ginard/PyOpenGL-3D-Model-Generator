#!/usr/bin/env python
# -*- coding: utf-8 -*-


from OpenGL.GL import *
import pyrr


class Buffer:

    @staticmethod
    def bind_vao():
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

    # copiar a la memoria el buffer de la figura
    @staticmethod
    def bind_vbo(vertexs_figure):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)  # vincular 2 buffers
        glBufferData(GL_ARRAY_BUFFER, vertexs_figure.nbytes, vertexs_figure, GL_STATIC_DRAW)

    # copiar a la memoria el buffer dels indexs
    @staticmethod
    def bind_ebo(indexs_figure):
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indexs_figure.nbytes, indexs_figure, GL_STATIC_DRAW)

    @staticmethod
    def get_atribut(shader, atribut):
        return glGetAttribLocation(shader, atribut)

    @staticmethod
    def vertex_attrib(nvertexs, offset):
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, nvertexs * 4, ctypes.c_void_p(offset))
        glEnableVertexAttribArray(0)  # 1 vertex són 3 coordenades float = 12 bytes
        # 0 o atribut ("position")    # si tenim normals, 1 vèrtex = 6 coordenades = 24 bytes
