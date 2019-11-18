#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy
from Figures.Figure import Figure


class Plane(Figure):

    def __init__(self):
        """ Defines plane's vertices and how they are linked (indexes)

        vertices:
            first 3 numpy: coordinate.
            last 3 numpy: normal vector (for each face)
        indexes: links between each vertex to form the faces.
        """
        Figure.__init__(self)

        self.vertices = [-0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
                         0.5, -0.5, 0.0,  0.0, 0.0, 1.0,
                         -0.5, 0.5, 0.0,  0.0, 0.0, 1.0,

                         0.5, -0.5, 0.0,  0.0, 0.0, 1.0,
                         -0.5, 0.5, 0.0,  0.0, 0.0, 1.0,
                         0.5, 0.5, 0.0,   0.0, 0.0, 1.0]

        self.indexes = [0, 1, 2,
                        3, 4, 5]

        self.vertices = numpy.array(self.vertices, numpy.float32)
        self.indexes = numpy.array(self.indexes, numpy.uint32)
