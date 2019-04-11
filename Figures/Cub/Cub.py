import numpy
from Buffer.Buffer import *
from Shaders import ShaderLoader
from Espai.Espai import *


class Cub:

    def __init__(self):
        self.vertexs = [-0.5, -0.5, -0.5,  0.0,  0.0, -1.0,
                         0.5, -0.5, -0.5,  0.0,  0.0, -1.0,
                         0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
                         0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
                        -0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
                        -0.5, -0.5, -0.5,  0.0,  0.0, -1.0,

                        -0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
                         0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
                         0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
                         0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
                        -0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
                        -0.5, -0.5,  0.5,  0.0,  0.0, 1.0,

                        -0.5,  0.5,  0.5, -1.0,  0.0,  0.0,
                        -0.5,  0.5, -0.5, -1.0,  0.0,  0.0,
                        -0.5, -0.5, -0.5, -1.0,  0.0,  0.0,
                        -0.5, -0.5, -0.5, -1.0,  0.0,  0.0,
                        -0.5, -0.5,  0.5, -1.0,  0.0,  0.0,
                        -0.5,  0.5,  0.5, -1.0,  0.0,  0.0,

                         0.5,  0.5,  0.5,  1.0,  0.0,  0.0,
                         0.5,  0.5, -0.5,  1.0,  0.0,  0.0,
                         0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
                         0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
                         0.5, -0.5,  0.5,  1.0,  0.0,  0.0,
                         0.5,  0.5,  0.5,  1.0,  0.0,  0.0,

                        -0.5, -0.5, -0.5,  0.0, -1.0,  0.0,
                         0.5, -0.5, -0.5,  0.0, -1.0,  0.0,
                         0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
                         0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
                        -0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
                        -0.5, -0.5, -0.5,  0.0, -1.0,  0.0,

                        -0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
                         0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
                         0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
                         0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
                        -0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
                        -0.5,  0.5, -0.5,  0.0,  1.0,  0.0]

        self.indexs = [0, 1, 2, 2, 3, 0,
                       4, 5, 6, 6, 7, 4,
                       7, 3, 0, 0, 4, 7,
                       6, 2, 1, 1, 5, 6,
                       0, 1, 5, 5, 4, 0,
                       3, 2, 6, 6, 7, 3]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

    def instanciar_cub(self, shader):
        Buffer.bind_vbo(self.vertexs)
        Buffer.bind_ebo(self.indexs)
        Buffer.get_atribut(shader, "position")
        Buffer.vertex_attrib(6, 0)
        Buffer.get_atribut(shader, "aNormal")
        Buffer.vertex_attrib(6, 144)

    @staticmethod
    def view_proj_cub(shader, view, proj):
        Espai.view_proj(shader, view, proj)

    def dibuixar_cub(self, shader, camera, proj, figure, vao):
        Espai.definir_figura(shader, camera, proj, figure)
        Espai.dibuixar_figura(vao, shader, self.indexs)
