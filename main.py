#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Figures.Pla.Pla import *
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

    # CUB
    cub = Cub()
    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader("Figures/Cub/vertex_shader.vs",
                                             "Figures/Cub/fragment_shader.fs")
    cub.instanciar_cub(cub_shader)

    # PIRAMIDE
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

    # general
    proj = Espai.proj(45.0, width, height, 0.1, 100.0)
    view = Espai.view(0.0, 0.0, -4.0)
    scale = Espai.scale(8.0, 1.0, 1.0)  # pla

    # cub
    glUseProgram(cub_shader)
    view_loc = glGetUniformLocation(cub_shader, "view")
    proj_loc = glGetUniformLocation(cub_shader, "proj")
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)
    glUseProgram(0)

    # piramide
    glUseProgram(pir_shader)
    view_loc_pir = glGetUniformLocation(pir_shader, "view")
    proj_loc_pir = glGetUniformLocation(pir_shader, "proj")
    glUniformMatrix4fv(view_loc_pir, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc_pir, 1, GL_FALSE, proj)
    glUseProgram(0)

    # pla
    glUseProgram(pla_shader)
    view_loc_pla = glGetUniformLocation(pla_shader, "view")
    proj_loc_pla = glGetUniformLocation(pla_shader, "proj")
    scale_loc_pla = glGetUniformLocation(pla_shader, "scale")
    glUniformMatrix4fv(view_loc_pla, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc_pla, 1, GL_FALSE, proj)
    glUniformMatrix4fv(scale_loc_pla, 1, GL_FALSE, scale)
    glUseProgram(0)

    # coordenades
    positions = [(2.0, 5.0, -15.0), (-1.5, 0.2, -2.5), (0.0, -2.0, -7.5)]

    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        Finestra.events()

        cub.dibuixar_cub(cub_vao, positions[1], cub_shader)
        pir.dibuixar_piramide(pir_vao, positions[0], pir_shader)
        pla.dibuixar_pla(pla_vao, positions[2], pla_shader)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
