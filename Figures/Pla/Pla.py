import numpy
from Buffer.Buffer import *
from Shaders import ShaderLoader
from Espai.Espai import *


class Pla:

    def __init__(self):
        self.vertexs = [-0.5, 0, -0.5,  0.5, 0, -0.5,
                        0.5, 0, 0.5,    -0.5, 0, 0.5]

        self.indexs = [0, 1, 3, 1, 2, 3]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

    def instanciar_pla(self, shader):
        Buffer.bind_vbo(self.vertexs)
        Buffer.bind_ebo(self.indexs)
        Buffer.get_atribut(shader, "position")
        Buffer.vertex_attrib(0)

    @staticmethod
    def view_proj_pla(shader, view, proj):
        Espai.view_proj(shader, view, proj)

    def dibuixar_pla(self, vao, posicio, shader):
        Espai.dibuixar_figura(vao, posicio, shader, self.indexs)
