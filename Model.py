#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Figures.Cube.Cube import *
from Figures.Pyramid.Pyramid import *
from Figures.Plane.Plane import *
from Figures.figure import Figure
from Figures.Buffer import *
from Shaders import ShaderLoader
from Window.Window import *
from Constants import *
import Random.Color as Color
import Render.Render as Render
import Space.Space as Space
import glfw
import random


def place_background(planes):
    """ Set background position and color.

    :param planes: objects to set.
    """
    x_rand = random.uniform(-2, 2)
    y_rand = random.uniform(-2, 1)
    background_color = Color.get_background_color()
    planes[0].set_figure([-1.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 0)
    planes[1].set_figure([-1.0 + x_rand, -5.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 90, 0)
    planes[2].set_figure([-7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)
    planes[3].set_figure([7.0 + x_rand, 3.0 + y_rand, -10.0], [16.0, 18.0, 10.0], background_color, 0, 90)


def draw_background(plane, shader, view, projection, planes, vao):
    """ Draws the background for the scene, representing the rooms' walls.

    :param plane: object to draw the planes.
    :param shader: figure's shader object.
    :param view: camera.
    :param projection: projection perspective matrix.
    :param planes: array of the planes to draw.
    :param vao: vertex array object.
    """
    plane.draw(shader, view, projection, planes[0], vao)
    plane.draw(shader, view, projection, planes[1], vao)
    plane.draw(shader, view, projection, planes[2], vao)
    plane.draw(shader, view, projection, planes[3], vao)


def capture_image(camera, fragment_shader, cubs, pyramids, path, img_size):
    """ Instance window, set all figure's attributes and draw them on the scene.

    :param camera: camera position.
    :param fragment_shader: figure's shader object.
    :param cubs: cubes to draw.
    :param pyramids: pyramids to draw.
    :param path: path where to store the images.
    :param img_size: image resolution.
    """

    """ Window initialization phase """
    initialize_attributes()
    window = create_window(img_size, img_size, "3D Scene")

    if not window:
        glfw.terminate()
        return

    make_context(window)
    set_window_background_color(0.7, 0.7, 0.7)

    # general
    projection = Space.set_projection(degrees=60.0,
                                      aspect_ratio=img_size/img_size,
                                      front_pane=0.1,
                                      back_pane=100.0)
    camera_view = Space.set_view(camera[0], camera[1])

    """ Figure's instance phase """
    cube = Cube()
    cube_vao = bind_vao()
    cube_shader = ShaderLoader.compile_shader(fragment_shader)
    cube.set_buffer(cube_shader, offset=144)

    pyramid = Pyramid()
    pyramid_vao = bind_vao()
    pyramid_shader = ShaderLoader.compile_shader(fragment_shader)
    pyramid.set_buffer(pyramid_shader, offset=48)

    plane = Plane()
    plane_vao = bind_vao()
    plane_shader = ShaderLoader.compile_shader(fragment_shader)
    plane.set_buffer(plane_shader, offset=24)

    back_plane = Figure()
    bottom_plane = Figure()
    left_plane = Figure()
    right_plane = Figure()
    planes = [back_plane, bottom_plane, left_plane, right_plane]
    place_background(planes)

    glEnable(GL_DEPTH_TEST)  # enables depth
    events()

    """ Drawing phase """
    draw_background(plane, plane_shader, camera_view, projection, planes, plane_vao)

    for figure in cubs:
        cube.draw(cube_shader, camera_view, projection, figure, cube_vao)

    for figure in pyramids:
        pyramid.draw(pyramid_shader, camera_view, projection, figure, pyramid_vao)

    Render.render_to_jpg(path)
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

    for i in range(initial_model, num_models + initial_model):
        print(i)

        cubes = get_figures(MIN_CUBS, MAX_CUBS)  # in order to have the exact same figures in each image
        pyramids = get_figures(MIN_PIRS, MAX_PIRS)

        capture_image(CENTER_CAMERA, DEPTH_FRAGMENT_SHADER, cubes, pyramids, path + DEPTH_PAHT + str(i) + "_d.png", img_size)
        capture_image(LEFT_CAMERA, FRAGMENT_SHADER, cubes, pyramids, path + LEFT_PATH + str(i) + "_l.jpg", img_size)
        capture_image(RIGHT_CAMERA, FRAGMENT_SHADER, cubes, pyramids, path + RIGHT_PATH + str(i) + "_r.jpg", img_size)
