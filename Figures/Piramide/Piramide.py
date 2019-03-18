import numpy
from Buffer.Buffer import *
from Shaders import ShaderLoader
from Espai.Espai import *

class Piramide:

    def __init__(self):
        self.vertexs = [0.0, 0.5, 0.0,   -0.5, -0.5, 0.5,
                        0.5, -0.5, 0.5,  0.0, -0.5, -0.5]

        self.indexs = [0, 1, 2,  0, 2, 3,
                       0, 1, 3,  1, 2, 3]

        self.vertexs = numpy.array(self.vertexs, numpy.float32)
        self.indexs = numpy.array(self.indexs, numpy.uint32)

