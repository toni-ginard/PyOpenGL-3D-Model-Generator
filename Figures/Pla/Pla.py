#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import Buffer.Buffer as Buffer
import Space.Space as Espai


class Pla:

    def __init__(self):
        self.vertexs = [-0.5, -0.5, 0.0,  0.0, 0.0, 1.0,
                        0.5,  -0.5, 0.0,  0.0, 0.0, 1.0,
                        -0.5, 0.5, 0.0,   0.0, 0.0, 1.0,

                        0.5, -0.5, 0.0,   0.0, 0.0, 1.0,
                        -0.5, 0.5, 0.0,   0.0, 0.0, 1.0,
                        0.5, 0.5, 0.0,    0.0, 0.0, 1.0]

        self.indexs = [0, 1, 2,
                       3, 4, 5]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

    def instanciar_pla(self, shader):
        Buffer.bind_vbo(self.vertexs)
        Buffer.bind_ebo(self.indexs)
        Buffer.get_attribute(shader, "position")
        Buffer.vertex_attribute(6, 0, 0)
        Buffer.get_attribute(shader, "aNormal")
        Buffer.vertex_attribute(6, 24, 1)

    def dibuixar_pla(self, shader, camera, proj, figura, vao):
        Espai.set_figure_attributes(shader, camera, proj, figura)
        Espai.draw_figure(shader, self.indexs, vao)
