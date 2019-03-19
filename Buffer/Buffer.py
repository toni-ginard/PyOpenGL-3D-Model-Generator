from OpenGL.GL import *
import pyrr


class Buffer:

    @staticmethod
    def bind_vao():
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

    # copiar a la memoria el buffer de la figura
    @staticmethod
    def bind_vbo(vertexs_figura):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)  # vincular 2 buffers
        glBufferData(GL_ARRAY_BUFFER, vertexs_figura.nbytes, vertexs_figura, GL_STATIC_DRAW)

    # copiar a la memoria el buffer dels indexs
    @staticmethod
    def bind_ebo(indexs_figura):
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indexs_figura.nbytes, indexs_figura, GL_STATIC_DRAW)

    @staticmethod
    def get_atribut(shader, atribut):
        return glGetAttribLocation(shader, atribut)

    @staticmethod
    def vertex_attrib(offset):
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(offset))
        glEnableVertexAttribArray(0)  # 1 vertex son 3 coordenades float = 12 bytes
        # 0 o atribut ("position")

