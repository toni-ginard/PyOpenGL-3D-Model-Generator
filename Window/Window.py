import glfw
from OpenGL.GL import *


def create_window(width, height, title):
    """ Create window and its context. """
    return glfw.create_window(width, height, title, None, None)


def initialize_attributes():
    """ Initialize glfw attributes. """
    glfw.init()
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)


def make_context(window):
    """ Make context for specified window. """
    glfw.make_context_current(window)


def set_window_background_color(r, g, b):
    """ Set window background color.
    :param float r: red value.
    :param float g: green value.
    :param float b: blue value.
    """
    glClearColor(r, g, b, 1.0)


def events():
    """ Process events. """
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
