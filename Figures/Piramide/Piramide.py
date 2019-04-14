import numpy
from Buffer.Buffer import *
from Shaders import ShaderLoader
from Espai.Espai import *


class Piramide:

    def __init__(self):
        self.vertexs = [0.0,   0.5, 0.0,   0.0, 0.5, 1.0,
                        -0.5, -0.5, 0.5,   0.0, 0.5, 1.0,
                        0.5,  -0.5, 0.5,   0.0, 0.5, 1.0,

                        0.0, 0.5, 0.0,     1.0, 0.25, -0.5,
                        0.5, -0.5, 0.5,    1.0, 0.25, -0.5,
                        0.0, -0.5, -0.5,   1.0, 0.25, -0.5,

                        0.0, 0.5, 0.0,     1.0, -0.25, 0.5,
                        -0.5, -0.5, 0.5,   1.0, -0.25, 0.5,
                        0.0, -0.5, -0.5,   1.0, -0.25, 0.5,

                        -0.5, -0.5, 0.5,   0.0, -1.0, 0.0,
                        0.5,  -0.5, 0.5,   0.0, -1.0, 0.0,
                        0.0, -0.5, -0.5,   0.0, -1.0, 0.0]

        self.indexs = [0, 1, 2,
                       0, 2, 3,
                       0, 1, 3,
                       1, 2, 3]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

    def instanciar_piramide(self, shader):
        Buffer.bind_vbo(self.vertexs)
        Buffer.bind_ebo(self.indexs)
        Buffer.get_atribut(shader, "position")
        Buffer.vertex_attrib(6, 0, 0)
        Buffer.get_atribut(shader, "aNormal")
        Buffer.vertex_attrib(6, 48, 1)

    def dibuixar_piramide(self, shader, camera, proj, figure, vao):
        Espai.definir_figura(shader, camera, proj, figure)
        Espai.dibuixar_figura(vao, shader, self.indexs)
