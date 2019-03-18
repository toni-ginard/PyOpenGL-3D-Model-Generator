import numpy
from Buffer.Buffer import *
from Shaders import ShaderLoader
from Espai.Espai import *


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

    def instanciar_cub(self):
        Buffer.bind_vao()
        cub_shader = ShaderLoader.compile_shader("Figures/Cub/vertex_shader.vs", "Figures/Cub/fragment_shader.fs")
        Buffer.bind_vbo(self.vertexs)
        Buffer.bind_ebo(self.indexs)
        # position = ...
        Buffer.get_atribut(cub_shader, "position")
        Buffer.vertex_attrib(0)
        # normals, textures...

        glUseProgram(cub_shader)
        return cub_shader

    @staticmethod
    def view_proj_cub(shader, view, proj):
        Espai.view_proj(shader, view, proj)

    @staticmethod
    def dibuixar_cub(posicio, shader, indexs_figura):
        Espai.dibuixar_figura(posicio, shader, indexs_figura)