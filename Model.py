#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Figures.Cube.Cube import *
from Figures.Pyramid.Pyramid import *
from Figures.Plane.Plane import *
import Figures.Buffer as Buffer
from Figures.Background import *
from Shaders import ShaderLoader
from Window.Window import *
from Constants.Constants import *
from Constants.Constants_Main import *
import Render.Render as Render
import glfw


def capture_scene(camera, fragment_shader, cubes, pyramids, path):
    """ Instance window, set all figure's attributes and draw them on the scene.

    :param camera: camera position.
    :param fragment_shader: figure's shader object.
    :param cubes: cubes to draw.
    :param pyramids: pyramids to draw.
    :param path: specific path where to store the images.
    """

    """ Window initialization phase """
    initialize_attributes()
    window = create_window(IMG_SIZE, IMG_SIZE, "3D Scene")

    if not window:
        glfw.terminate()
        return

    make_context(window)
    set_window_background_color(0.7, 0.7, 0.7)

    """ Figure's instance phase """
    cube = Cube()
    cube_vao = Buffer.bind_vao()
    cube_shader = ShaderLoader.compile_shader(fragment_shader)
    cube.set_buffer(cube_shader, offset=144)

    pyramid = Pyramid()
    pyramid_vao = Buffer.bind_vao()
    pyramid_shader = ShaderLoader.compile_shader(fragment_shader)
    pyramid.set_buffer(pyramid_shader, offset=48)

    plane = Plane()
    plane_vao = Buffer.bind_vao()
    plane_shader = ShaderLoader.compile_shader(fragment_shader)
    plane.set_buffer(plane_shader, offset=24)

    background = Background()
    background.set_background()

    glEnable(GL_DEPTH_TEST)  # enables depth
    events()

    """ Drawing phase """
    background.draw_background(plane, plane_shader, camera, plane_vao)

    for attributes in cubes:
        cube.draw(cube_shader, camera, attributes, cube_vao)

    for attributes in pyramids:
        pyramid.draw(pyramid_shader, camera, attributes, pyramid_vao)

    """ Render phase """
    Render.render_to_jpg(MAIN_PATH + path)
    glfw.terminate()


def generate_models():
    """ Generates figure's attributes, sets up the scenes and captures a stereoscopic image and its corresponding
    depth image. """
    for i in range(INITIAL_SCENE, NUM_SCENES + INITIAL_SCENE):
        print(i)

        cubes = Figure.get_random_figures(NUM_CUBES)  # in order to have the exact same figures in each image
        pyramids = Figure.get_random_figures(NUM_PYRAMIDS)

        capture_scene(CENTER_CAMERA, DEPTH_FRAGMENT_SHADER, cubes, pyramids, "/depth/depth/" + str(i) + "_d.jpg")
        capture_scene(LEFT_CAMERA,   FRAGMENT_SHADER,       cubes, pyramids, "/left/left/" + str(i) + "_l.jpg")
        capture_scene(RIGHT_CAMERA,  FRAGMENT_SHADER,       cubes, pyramids, "/right/right/" + str(i) + "_r.jpg")
