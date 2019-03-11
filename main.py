#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glfw
import numpy
from PIL import Image

from Finestra import Finestra
from Render.Render import Render
from Obj.ObjLoader import *
from OpenGL_Operations import *
from Shaders import ShaderLoader
from Figures.Cub import Cub


width = 640
height = 480


def main():

    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)

    cub = Cub()

    Shader.bind_vao()  # genèric

    # compilar shaders
    shader = ShaderLoader.compile_shader("Shaders/vertex_shader.vs", "Shaders/fragment_shader.fs")

    Shader.bind_vbo(cub.vertexs)  # cub.vertes
    Shader.bind_ebo(cub.indexs)

    # position = ...
    Shader.get_atribut(shader, "position")
    Shader.vertex_attrib(0)

    glUseProgram(shader)
    glClearColor(0.7, 0.7, 0.7, 1.0)  # color fons
    glEnable(GL_DEPTH_TEST)  # profunditat

    # matrius (model -> view -> projection)
    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -4.0]))
    proj = pyrr.matrix44.create_perspective_projection_matrix(45.0, width / height, 0.1, 100.0)

    view_loc = glGetUniformLocation(shader, "view")
    proj_loc = glGetUniformLocation(shader, "proj")
    # light_loc = glUniformMatrix4fv(shader, "light")

    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)

    # model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
    # glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    cube_positions = [(2.0, 5.0, -15.0), (-1.5, -1.2, -2.5)]

    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i in range(len(cube_positions)):
            model_loc = glGetUniformLocation(shader, "model")
            model = pyrr.matrix44.create_from_translation(cube_positions[i])
            glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
            glDrawElements(GL_TRIANGLES, cub.indexs.size, GL_UNSIGNED_INT, None)

        # glUniformMatrix4fv(light_loc, 1, GL_FALSE, light)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
