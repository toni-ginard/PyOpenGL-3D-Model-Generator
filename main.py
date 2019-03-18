#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Buffer.Buffer import *
from Espai.Espai import Espai

width = 640
height = 480


def main():

    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)
    Finestra.color_fons(0.7, 0.7, 0.7)

    cub = Cub()
    # cub_shader = cub.instanciar_cub()

    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader("Figures/Cub/vertex_shader.vs", "Figures/Cub/fragment_shader.fs")
    cub_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cub_vbo)  # vincular 2 buffers
    glBufferData(GL_ARRAY_BUFFER, cub.vertexs.nbytes, cub.vertexs, GL_STATIC_DRAW)
    cub_ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, cub_ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, cub.indexs.nbytes, cub.indexs, GL_STATIC_DRAW)
    glGetAttribLocation(cub_shader, "position")
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    pir = Piramide()
    pir_vao = glGenVertexArrays(1)
    glBindVertexArray(pir_vao)
    pir_shader = ShaderLoader.compile_shader("Figures/Piramide/vertex_shader.vs", "Figures/Piramide/fragment_shader.fs")
    pir_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pir_vbo)
    glBufferData(GL_ARRAY_BUFFER, pir.vertexs.nbytes, pir.vertexs, GL_STATIC_DRAW)
    pir_ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, pir_ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, pir.indexs.nbytes, pir.indexs, GL_STATIC_DRAW)
    glGetAttribLocation(pir_shader, "position")
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    proj = pyrr.matrix44.create_perspective_projection_matrix(45.0, width / height, 0.1, 100.0)

    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -4.0]))

    glUseProgram(cub_shader)
    view_loc = glGetUniformLocation(cub_shader, "view")
    proj_loc = glGetUniformLocation(cub_shader, "proj")
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)

    glUseProgram(pir_shader)
    view_loc_pir = glGetUniformLocation(pir_shader, "view")
    proj_loc_pir = glGetUniformLocation(pir_shader, "proj")
    glUniformMatrix4fv(view_loc_pir, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc_pir, 1, GL_FALSE, proj)

    cube_positions = [(2.0, 5.0, -15.0), (-1.5, -1.2, -2.5), (1.0, -0.0, -4.0)]

    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        Finestra.events()

        # for i in range(len(cube_positions)):
            # Cub.dibuixar_cub(cube_positions[i], cub_shader, cub.indexs)
        model = pyrr.matrix44.create_from_translation(cube_positions[0])
        model_loc = glGetUniformLocation(cub_shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, cub.indexs.size, GL_UNSIGNED_INT, None)

        model_pir = pyrr.matrix44.create_from_translation(cube_positions[1])
        model_loc_pir = glGetUniformLocation(pir_shader, "model")
        glUniformMatrix4fv(model_loc_pir, 1, GL_FALSE, model_pir)
        glDrawElements(GL_TRIANGLES, pir.indexs.size, GL_UNSIGNED_INT, None)


        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
