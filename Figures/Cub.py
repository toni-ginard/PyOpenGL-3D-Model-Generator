import numpy


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



