#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Figures.Pla.Pla import *
from Figures.figura import Figura
from Buffer.Buffer import *
from Espai.Espai import Espai
import random


width = 640
height = 480

# nº figures
max_cubs = 13
min_cubs = 10
max_pirs = 13
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
    camera = Espai.view([0.0, 0.0, 5.0], [0.0, 0.0, 0.0])

    # CUB
    cub = Cub()
    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader("Shaders/vertex_shader.vs", "Shaders/fragment_shader.fs")
    cub.instanciar_cub(cub_shader)
    # PIRÀMIDE
    pir = Piramide()
    pir_vao = glGenVertexArrays(1)
    glBindVertexArray(pir_vao)
    pir_shader = ShaderLoader.compile_shader("Shaders/vertex_shader.vs", "Shaders/fragment_shader.fs")
    pir.instanciar_piramide(pir_shader)
    # PLA
    pla = Pla()
    pla_vao = glGenVertexArrays(1)
    glBindVertexArray(pla_vao)
    pla_shader = ShaderLoader.compile_shader("Shaders/vertex_shader.vs", "Shaders/fragment_shader.fs")
    pla.instanciar_pla(pla_shader)

    # AUTOMATITZACIÓ
    ncubs = random.randrange(min_cubs, max_cubs, 1) * 2
    cubs = Figura.get_figures(ncubs)

    npiramides = random.randrange(min_pirs, max_pirs, 1) * 2
    piramides = Figura.get_figures(npiramides)

    pla_fons = Figura()
    pla_fons.set_figura([2.0, 3.0, -10.0], [20.0, 18.0, 10.0], [0.4, 0.4, 0.4])

    glEnable(GL_DEPTH_TEST)  # profunditat

    #while not glfw.window_should_close(window):
    Finestra.events()

        # paràmetres: shader, view proj (camera), ubicació, scale (canvi mida), color

        # pla fons
    pla.dibuixar_pla(pla_shader, camera, proj, pla_fons, pla_vao)

    for figura in cubs:
        cub.dibuixar_cub(cub_shader, camera, proj, figura, cub_vao)

    for figura in piramides:
        pir.dibuixar_piramide(pir_shader, camera, proj, figura, pir_vao)

    # glfw.swap_buffers(window)

    Render.render_to_jpg()
    #glfw.terminate()


if __name__ == "__main__":
    main()
