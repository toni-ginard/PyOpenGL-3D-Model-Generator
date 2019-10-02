#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Figures.Cube.Cube import *
from Figures.Piramide.Pyramid import *
from Figures.Pla.Plane import *
from Figures.figure import Figure
from Shaders import ShaderLoader
from Random.Color import Color
from OpenGL.GL import *
import Render.Render as Render
import Space.Space as Space
import Window.Window as Window
import glfw
import random


# nº figures
MIN_CUBS = 5
MAX_CUBS = 10
MIN_PIRS = 5
MAX_PIRS = 10


def capture_image(eye, target, vertex_shader, fragment_shader, cubs, piramides, nom_img, path, img_size):
    Window.initialize_attributes()
    window = Window.create_window(img_size, img_size, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Window.make_context(window)
    Window.background_color(0.7, 0.7, 0.7)

    # general
    projection = Space.set_projection(degrees=60.0,
                                      aspect_ratio=img_size/img_size,
                                      front_pane=0.1,
                                      back_pane=100.0)
    camera = Space.set_view(eye, target)

    # CUB
    cub = Cube()
    cub_vao = glGenVertexArrays(1)
    glBindVertexArray(cub_vao)
    cub_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    cub.set_buffer(cub_shader, offset=144)
    # PIRÀMIDE
    pir = Pyramid()
    pir_vao = glGenVertexArrays(1)
    glBindVertexArray(pir_vao)
    pir_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    pir.set_buffer(pir_shader, offset=48)
    # PLA
    pla = Plane()
    pla_vao = glGenVertexArrays(1)
    glBindVertexArray(pla_vao)
    pla_shader = ShaderLoader.compile_shader(vertex_shader, fragment_shader)
    pla.set_buffer(pla_shader, offset=24)

    # AUTOMATITZACIÓ
    # instanciar fons
    x_rand = random.uniform(-2, 2)
    y_rand = random.uniform(-2, 1)
    pla_back = Figure()
    pla_bottom = Figure()
    pla_left = Figure()
    pla_right = Figure()
    background_color = Color.get_background_color()
    pla_back.set_figure([-1.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 0)
    pla_bottom.set_figure([-1.0 + x_rand, -5.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 90, 0)
    pla_left.set_figure([-7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)
    pla_right.set_figure([7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)

    glEnable(GL_DEPTH_TEST)  # enables depth
    Window.events()

    # draw background
    pla.draw(pla_shader, camera, projection, pla_back, pla_vao)
    pla.draw(pla_shader, camera, projection, pla_bottom, pla_vao)
    pla.draw(pla_shader, camera, projection, pla_left, pla_vao)
    pla.draw(pla_shader, camera, projection, pla_right, pla_vao)

    for figura in cubs:
        cub.draw(cub_shader, camera, projection, figura, cub_vao)

    for figura in piramides:
        pir.draw(pir_shader, camera, projection, figura, pir_vao)

    Render.render_to_jpg(nom_img, path)
    glfw.terminate()


def get_figures(min, max):
    """ Returns random number of figures, each one with random attributes.

    :param min: minimum number of figures.
    :param max: maximum number of figures.
    :rtype: numpy.array
    :return: array of figures.
    """
    nfigures = random.randrange(min, max, 1) * 2
    return Figure.get_random_figures(nfigures)


def create_model(path, num_models, initial_model, img_size):
    """ Sets up 3 cameras to capture a stereoscopic image and its corresponding depth image.

    :param path: path to store the images.
    :param num_models: number of models to create.
    :param initial_model: initial model number.
    :param img_size: resolution of the image.
    """
    vs = "Shaders/vertex_shader.vs"
    fs = "Shaders/fragment_shader.fs"
    dfs = "Shaders/depth_fragment_shader.fs"

    center = [0.0, 0.0, 5.0]
    center_target = [0.0, 0.0, 0.0]

    left = [-0.05, 0.0, 5.0]
    left_target = [-0.05, 0.0, 0.0]

    right = [0.05, 0.0, 5.0]
    right_target = [0.05, 0.0, 0.0]

    for i in range(initial_model, num_models + initial_model):
        print(i)
        img = "esc" + str(i)

        cubes = get_figures(MIN_CUBS, MAX_CUBS)  # in order to have the exact same figures in each image
        pyramids = get_figures(MIN_PIRS, MAX_PIRS)

        capture_image(center, center_target, vs, dfs, cubes, pyramids, img + "_d.jpg", path + "/depth/depth", img_size)
        # capture_image(center, center_target, vs, fs,  cubes, pyramids, img + "_drgb.jpg", path + "/depthrgb/depthrgb")
        capture_image(left,   left_target, vs, fs, cubes, pyramids, img + "_l.jpg", path + "/left/left", img_size)
        capture_image(right,  right_target, vs, fs, cubes, pyramids, img + "_r.jpg", path + "/right/right", img_size)
