#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import *
from Figures.Piramide.Piramide import *
from Figures.Pla.Pla import *
from Figures.figure import Figure
from Buffer.Buffer import *
from Espai.Espai import Espai
import random


width = 640
height = 480

# nº figures
min_cubs = 5
max_cubs = 10
min_pirs = 5
max_pirs = 10

vs = "Shaders/vertex_shader.vs"
fs = "Shaders/fragment_shader.fs"
dfs = "Shaders/depth_fragment_shader.fs"


def capturar_imatge(eye, target, vertex_shader, fragment_shader, cubs, piramides, nom_img):
    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)
    Finestra.color_fons(0.7, 0.7, 0.7)

    # general
    proj = Espai.proj(60.0, width, height, 0.1, 100.0)
    camera = Espai.view(eye, target)

    # CUB
    cub = Cub()
    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    cub.instanciar_cub(cub_shader)
    # PIRÀMIDE
    pir = Piramide()
    pir_vao = glGenVertexArrays(1)
    glBindVertexArray(pir_vao)
    pir_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    pir.instanciar_piramide(pir_shader)
    # PLA
    pla = Pla()
    pla_vao = glGenVertexArrays(1)
    glBindVertexArray(pla_vao)
    pla_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    pla.instanciar_pla(pla_shader)

    # AUTOMATITZACIÓ
    pla_fons = Figure()
    pla_fons.set_figure([2.0, 3.0, -10.0], [20.0, 18.0, 10.0], [0.4, 0.4, 0.4], 0, 0)

    glEnable(GL_DEPTH_TEST)  # profunditat

    Finestra.events()

    pla.dibuixar_pla(pla_shader, camera, proj, pla_fons, pla_vao)

    for figura in cubs:
        cub.dibuixar_cub(cub_shader, camera, proj, figura, cub_vao)

    # for figura in piramides:
    #     pir.dibuixar_piramide(pir_shader, camera, proj, figura, pir_vao)

    Render.render_to_jpg(nom_img)
    glfw.terminate()


def get_random_figures(min, max):
    nfigures = random.randrange(min, max, 1) * 2
    return Figure.get_random_atrib_figures(nfigures)


def crear_model(num_models):
    center = [0.0, 0.0, 5.0]
    center_target = [0.0, 0.0, 0.0]

    left = [-0.05, 0.0, 5.0]
    left_target = [-0.05, 0.0, 0.0]

    right = [0.05, 0.0, 5.0]
    right_target = [0.05, 0.0, 0.0]

    for i in range(num_models):
        img = "esc" + str(i)

        cubs = get_random_figures(min_cubs, max_cubs)
        piramides = get_random_figures(min_pirs, max_pirs)

        capturar_imatge(center, center_target, vs, dfs, cubs, piramides, img + "_d.jpg")
        capturar_imatge(left,   left_target,   vs, fs,  cubs, piramides, img + "_l.jpg")
        capturar_imatge(right,  right_target,  vs, fs,  cubs, piramides, img + "_r.jpg")
