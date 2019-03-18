import numpy
from OpenGL.GL import *


class Cub:

    def __init__(self):
        self.vertexs = [-0.5, -0.5, 0.5,    0.5, -0.5, 0.5,
                        0.5, 0.5, 0.5,      -0.5, 0.5, 0.5,
                        -0.5, -0.5, -0.5,   0.5, -0.5, -0.5,
                        0.5, 0.5, -0.5,     -0.5, 0.5, -0.5]

        self.indexs = [0, 1, 2, 2, 3, 0,
                       4, 5, 6, 6, 7, 4,
                       4, 5, 1, 1, 0, 4,
                       6, 7, 3, 3, 2, 6,
                       5, 6, 2, 2, 1, 5,
                       7, 4, 0, 0, 3, 7]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

    @staticmethod
    def bind_vao():
        cub_vao = glGenVertexArrays(1)
        glBindVertexArray(cub_vao)

    # copiar a la memoria el buffer de la figura
    def bind_vbo(self):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)  # vincular 2 buffers
        glBufferData(GL_ARRAY_BUFFER, self.vertexs.nbytes, self.vertexs, GL_STATIC_DRAW)

    # copiar a la memoria el buffer dels indexs
    def bind_ebo(self):
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indexs.nbytes, self.indexs, GL_STATIC_DRAW)

    @staticmethod
    def get_atribut(shader, atribut):
        return glGetAttribLocation(shader, atribut)

    @staticmethod
    def vertex_attrib():
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)  # 1 vertex son 3 coordenades float = 12 bytes
        # 0 o atribut ("position"), offset = 0
