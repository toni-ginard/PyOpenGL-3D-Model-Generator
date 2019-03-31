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

    # general
    proj = Espai.proj(60.0, width, height, 0.1, 100.0)
    view = Espai.view()  # camera

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

    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        Finestra.events()

        # paràmetres: shader, view proj (camera), ubicació, scale (canvi mida), graus

        # pla fons
        Espai.definir_ubicacio(pla_shader, view, proj, [0.0, 0.0, -10.0], [10.0, 10.0, 100.0], 0)
        pla.dibuixar_pla(pla_vao, pla_shader)

        # cub
        Espai.definir_ubicacio(cub_shader, view, proj, [6.0, 6.0, -1.0], [0.5, 0.5, 0.5], 0)
        cub.dibuixar_cub(cub_vao, cub_shader)

        # piramide
        Espai.definir_ubicacio(pir_shader, view, proj, [-1.5, 2.0, -2.5], [1.0, 1.0, 1.0], 0)
        pir.dibuixar_piramide(pir_vao, pir_shader)

        # piramide 2
        Espai.definir_ubicacio(pir_shader, view, proj, [1.0, -0.5, 1.0], [1.0, 1.0, 1.0], 0)
        pir.dibuixar_piramide(pir_vao, pir_shader)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
