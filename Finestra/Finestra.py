import glfw
from OpenGL.GL import *


class Finestra:

    @staticmethod
    def instanciar(width, height, titol):
        return glfw.create_window(width, height, titol, None, None)

    # coses de glfw
    @staticmethod
    def initialize_attributes():
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    @staticmethod
    def make_context(finestra):
        glfw.make_context_current(finestra)

    @staticmethod
    def background_color(r, g, b):
        glClearColor(r, g, b, 1.0)

    @staticmethod
    def events():
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
