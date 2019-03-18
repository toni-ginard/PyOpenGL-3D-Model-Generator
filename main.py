#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glfw
import pyrr

from OpenGL.GL import *
from Finestra import Finestra
from Render.Render import Render
from Shaders import ShaderLoader
from Figures.Cub.Cub import Cub


width = 640
height = 480


def main():

    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)

    # CREACIÓ I INSTANCIACIÓ D'UN CUB
    cub = Cub()
    Cub.bind_vao()
    cub_shader = ShaderLoader.compile_shader("Figures/Cub/vertex_shader.vs", "Figures/Cub/fragment_shader.fs")
    cub.bind_vbo()
    cub.bind_ebo()
    # position = ...
    Cub.get_atribut(cub_shader, "position")
    Cub.vertex_attrib()
    # normals, textures...

    # matrius (model -> view -> projection)
    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -4.0]))
    proj = pyrr.matrix44.create_perspective_projection_matrix(45.0, width / height, 0.1, 100.0)

    glUseProgram(cub_shader)

    view_loc = glGetUniformLocation(cub_shader, "view")
    proj_loc = glGetUniformLocation(cub_shader, "proj")

    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)

    cube_positions = [(2.0, 5.0, -15.0), (-1.5, -1.2, -2.5), (1.0, -0.0, -4.0)]

    Finestra.color_fons(0.7, 0.7, 0.7)
    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i in range(len(cube_positions)):
            model_loc = glGetUniformLocation(cub_shader, "model")
            model = pyrr.matrix44.create_from_translation(cube_positions[i])  #
            glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)  #
            glDrawElements(GL_TRIANGLES, cub.indexs.size, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
