#!/usr/bin/env python
# -*- coding: utf-8 -*-


from OpenGL.GL import *
from Constants.Constants import *
import OpenGL.GL.shaders
import os


def load_shader(shader_file):
    """ Load shaders' files.
    :param shader_file: file to load.
    """
    os.chdir("/Users/toniginard/PycharmProjects/Generador-Models-3D")
    with open(shader_file) as f:
        shader_source = f.read()
    f.close()
    return str.encode(shader_source)


def compile_shader(fs):
    """ Create a new program, attach shaders and validate.
    :param vs: vertext shader file.
    :param fs: fragment shader file.
    :return: shader compiled.
    """
    vertex_shader = load_shader(VERTEX_SHADER)
    fragment_shader = load_shader(fs)

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    return shader
