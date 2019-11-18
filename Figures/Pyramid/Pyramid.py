#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy
from Figures.Figure import Figure


class Pyramid(Figure):

    def __init__(self):
        """
        Defines pyramid's vertices and how they are linked (indexes)

        vertices:
            first 3 numpy: coordinate.
            last 3 numpy: normal vector (for each face)
        indexes: links between each vertex to form the faces.
        """
        Figure.__init__(self)
        
        self.vertices = [0.0, 0.5, 0.0,   0.0, 0.5, 1.0,
                         -0.5, -0.5, 0.5, 0.0, 0.5, 1.0,
                         0.5, -0.5, 0.5,  0.0, 0.5, 1.0,

                         0.0, 0.5, 0.0,   1.0, 0.25, -0.5,
                         0.5, -0.5, 0.5,  1.0, 0.25, -0.5,
                         0.0, -0.5, -0.5, 1.0, 0.25, -0.5,

                         0.0, 0.5, 0.0,   -1.0, 0.25, -0.5,
                         -0.5, -0.5, 0.5, -1.0, 0.25, -0.5,
                         0.0, -0.5, 0.5,  -1.0, 0.25, -0.5,

                         -0.5, -0.5, 0.5,  0.0, -1.0, 0.0,
                         0.5, -0.5, 0.5,   0.0, -1.0, 0.0,
                         0.0, -0.5, -0.5,  0.0, -1.0, 0.0]

        self.indexes = [0, 1, 2,
                        0, 2, 3,
                        0, 1, 3,
                        1, 2, 3]

        self.vertices = numpy.array(self.vertices, numpy.float32)
        self.indexes = numpy.array(self.indexes, numpy.uint32)
