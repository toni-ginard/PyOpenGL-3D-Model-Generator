import numpy
import Buffer.Buffer as Buffer
import Space.Space as Space


class Cub:

    def __init__(self):
        """
        Defines cube's vertices and how they are linked (indexes)

        vertices:
            first 3 numpy: coordinate.
            last 3 numpy: normal vector (for each face)
        indexes: links between each vertex to form the faces. Each line is a face,
            formed by 2 triangles.
        """
        self.vertices = [-0.5, -0.5, -0.5, 0.0, 0.0, -1.0,
                         0.5,  -0.5, -0.5, 0.0, 0.0, -1.0,
                         0.5, 0.5, -0.5, 0.0, 0.0, -1.0,
                         0.5, 0.5, -0.5, 0.0, 0.0, -1.0,
                         -0.5, 0.5, -0.5, 0.0, 0.0, -1.0,
                         -0.5, -0.5, -0.5, 0.0, 0.0, -1.0,

                         -0.5, -0.5, 0.5, 0.0, 0.0, 1.0,
                         0.5, -0.5, 0.5, 0.0, 0.0, 1.0,
                         0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                         0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                         -0.5, 0.5, 0.5, 0.0, 0.0, 1.0,
                         -0.5, -0.5, 0.5, 0.0, 0.0, 1.0,

                         -0.5, 0.5, 0.5, -1.0, 0.0, 0.0,
                         -0.5, 0.5, -0.5, -1.0, 0.0, 0.0,
                         -0.5, -0.5, -0.5, -1.0, 0.0, 0.0,
                         -0.5, -0.5, -0.5, -1.0, 0.0, 0.0,
                         -0.5, -0.5, 0.5, -1.0, 0.0, 0.0,
                         -0.5, 0.5, 0.5, -1.0, 0.0, 0.0,

                         0.5, 0.5, 0.5, 1.0, 0.0, 0.0,
                         0.5, 0.5, -0.5, 1.0, 0.0, 0.0,
                         0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
                         0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
                         0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
                         0.5, 0.5, 0.5, 1.0, 0.0, 0.0,

                         -0.5, -0.5, -0.5, 0.0, -1.0, 0.0,
                         0.5, -0.5, -0.5, 0.0, -1.0, 0.0,
                         0.5, -0.5, 0.5, 0.0, -1.0, 0.0,
                         0.5, -0.5, 0.5, 0.0, -1.0, 0.0,
                         -0.5, -0.5, 0.5, 0.0, -1.0, 0.0,
                         -0.5, -0.5, -0.5, 0.0, -1.0, 0.0,

                         -0.5, 0.5, -0.5, 0.0, 1.0, 0.0,
                         0.5, 0.5, -0.5, 0.0, 1.0, 0.0,
                         0.5, 0.5, 0.5, 0.0, 1.0, 0.0,
                         0.5, 0.5, 0.5, 0.0, 1.0, 0.0,
                         -0.5, 0.5, 0.5, 0.0, 1.0, 0.0,
                         -0.5, 0.5, -0.5, 0.0, 1.0, 0.0]

        self.indexes = [0, 1, 2, 2, 3, 0,
                        4, 5, 6, 6, 7, 4,
                        7, 3, 0, 0, 4, 7,
                        6, 2, 1, 1, 5, 6,
                        0, 1, 5, 5, 4, 0,
                        3, 2, 6, 6, 7, 3]

        self.vertices = numpy.array(self.vertices, numpy.float32)
        self.indexes = numpy.array(self.indexes, numpy.uint32)

    def set_cube_attributes(self, shader):
        """ Sets all cubes' attributes in order to draw it.

        :param shader: figure's shader object.
        """
        Buffer.bind_vbo(self.vertices)
        Buffer.bind_ebo(self.indexes)
        Buffer.get_attribute(shader, "position")
        Buffer.vertex_attribute(6, 0, 0)
        Buffer.get_attribute(shader, "aNormal")
        Buffer.vertex_attribute(6, 144, 1)

    def draw_cube(self, shader, view, projection, figure, vao):
        """

        :param shader: figure's shader object.
        :param numpy.array view: camera coordinates.
        :param nunpy.array projection: perspective projection matrix.
        :param figure: object to set attributes and to draw.
        :param vao: vertex array object.
        """
        Space.set_figure_attributes(shader, view, projection, figure)
        Space.draw_figure(shader, self.indexes, vao)
