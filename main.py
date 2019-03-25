#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Figures.Pla.Pla import *
from Buffer.Buffer import *
from Espai.Espai import Espai
import math


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

    # coordenades
    positions = [(2.0, 2.0, -3.0), (-1.5, 2.0, -2.5), (0.0, 0.0, -5.0)]
    # general
    proj = Espai.proj(60.0, width, height, 0.1, 100.0)
    view = Espai.view(0.0, 0.0, 5.0)  # camera

    # CUB
    cub = Cub()
    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader("Figures/Cub/vertex_shader.vs",
                                             "Figures/Cub/fragment_shader.fs")
    cub.instanciar_cub(cub_shader)

    # PIRÀMIDE
    pir = Piramide()
    pir_vao = glGenVertexArrays(1)
    glBindVertexArray(pir_vao)
    pir_shader = ShaderLoader.compile_shader("Figures/Piramide/vertex_piramide.vs",
                                             "Figures/Piramide/fragment_piramide.fs")
    pir.instanciar_piramide(pir_shader)

    # PLA
    pla = Pla()
    pla_vao = glGenVertexArrays(1)
    glBindVertexArray(pla_vao)
    pla_shader = ShaderLoader.compile_shader("Figures/Pla/vertex_pla.vs",
                                             "Figures/Pla/fragment_pla.fs")
    pla.instanciar_pla(pla_shader)

    # cub
    glUseProgram(cub_shader)
    Espai.view_loc(cub_shader, view)
    Espai.proj_loc(cub_shader, proj)
    Espai.model(positions[0], cub_shader)
    glUseProgram(0)

    # piramide
    glUseProgram(pir_shader)
    Espai.view_loc(pir_shader, view)
    Espai.proj_loc(pir_shader, proj)
    Espai.model(positions[1], pir_shader)
    glUseProgram(0)

    # pla
    glUseProgram(pla_shader)
    Espai.view_loc(pla_shader, view)
    Espai.proj_loc(pla_shader, proj)
    Espai.model(positions[2], pla_shader)
    Espai.scale(pla_shader, 8.0, 8.0, 1.0)
    glUseProgram(0)

    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        Finestra.events()

        cub.dibuixar_cub(cub_vao, cub_shader)
        pir.dibuixar_piramide(pir_vao, pir_shader)
        pla.dibuixar_pla(pla_vao, pla_shader)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
