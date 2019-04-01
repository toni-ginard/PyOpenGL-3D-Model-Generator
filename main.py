#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Figures.Pla.Pla import *
from Buffer.Buffer import *
from Espai.Espai import Espai
from Positions.Position import *
import random


width = 640
height = 480

# nº figures
max_cubs = 15
min_cubs = 10
max_pirs = 15
min_pirs = 10


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

    # AUTOMATITZACIÓ
    ncubs = random.randrange(min_cubs, max_cubs, 1) * 2
    npir = random.randrange(min_pirs, max_pirs, 1) * 2

    coord_cubs = Position.array_posicions(ncubs)
    coord_pirs = Position.array_posicions(npir)

    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):
        Finestra.events()

        # paràmetres: shader, view proj (camera), ubicació, scale (canvi mida), graus (y)

        # pla fons
        Espai.definir_ubicacio(pla_shader, view, proj, [0.0, 0.0, -10.0], [10.0, 10.0, 1.0], 0)
        pla.dibuixar_pla(pla_vao, pla_shader)

        # cubs
        for coord in coord_cubs:
            Espai.definir_ubicacio(cub_shader, view, proj, coord, [1.0, 1.0, 1.0], 0)
            cub.dibuixar_cub(cub_vao, cub_shader)

        # piramides
        for coord in coord_pirs:
            Espai.definir_ubicacio(pir_shader, view, proj, coord, [1.0, 1.0, 1.0], 0)
            pir.dibuixar_piramide(pir_vao, pir_shader)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
