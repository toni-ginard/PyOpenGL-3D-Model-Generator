#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glfw
import numpy
from PIL import Image

from Finestra import Finestra
from Render.Render import Render
from Obj.ObjLoader import *
from OpenGL_Operations import *
from Shaders import ShaderLoader


width = 640
height = 480


def main():

    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)

    obj = ObjLoader()
    obj.load_model("res/cube.obj")

    texture_offset = len(obj.vertex_index) * 12
    normal_offset = texture_offset + len(obj.texture_index) * 2 * 4

    Shader.bind_vao()  # genèric

    # compilar shaders
    shader = ShaderLoader.compile_shader("Shaders/vertex_shader.vs", "Shaders/fragment_shader.fs")

    # VBO
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, obj.model.itemsize * len(obj.model), obj.model, GL_STATIC_DRAW)

    # position
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj.model.itemsize * 3, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    # texture
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj.model.itemsize * 2, ctypes.c_void_p(texture_offset))
    glEnableVertexAttribArray(1)
    # normals
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj.model.itemsize * 3, ctypes.c_void_p(normal_offset))
    glEnableVertexAttribArray(2)

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    # Set the texture wrapping parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # Set texture filtering parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    # load texture image
    image = Image.open("res/cube_texture.jpg")
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = numpy.array(list(flipped_image.getdata()), numpy.uint8)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    # glEnable(GL_TEXTURE_2D)

    glUseProgram(shader)
    glClearColor(0.7, 0.7, 0.7, 1.0)  # color fons
    glEnable(GL_DEPTH_TEST)  # profunditat
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # matrius (model -> view -> projection)
    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, -7.0, -3.0]))
    proj = pyrr.matrix44.create_perspective_projection_matrix(60.0, width / height, 0.1, 100.0)
    model = pyrr.matrix44.create_from_translation(pyrr.Vector3([2.0, 5.0, -10.0]))
    light = pyrr.matrix44.create_from_translation(pyrr.Vector3([-2.0, -2.0, 0.0]))

    view_loc = glGetUniformLocation(shader, "view")
    proj_loc = glGetUniformLocation(shader, "proj")
    model_loc = glGetUniformLocation(shader, "model")
    light_loc = glGetUniformLocation(shader, "light")

    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)


    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUniformMatrix4fv(light_loc, 1, GL_FALSE, light)

        glDrawArrays(GL_TRIANGLES, 0, len(obj.vertex_index))

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
