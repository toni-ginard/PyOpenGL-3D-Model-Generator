#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Finestra.Finestra import *
from Render.Render import Render
from Figures.Cub.Cub import Cub
from Buffer.Buffer import *
from Espai.Espai import Espai

width = 640
height = 480


def main():

    Finestra.inicialitzar_atributs()
    window = Finestra.instanciar(width, height, "Escena 3D")

    if not window:
        glfw.terminate()
        return

    Finestra.make_context(window)

    # CREACIÓ I INSTANCIACIÓ D'UN CUB
    cub = Cub()
    cub_shader = cub.instanciar_cub()

    # matrius (model -> view -> projection)
    proj = Espai.proj(45.0, width, height, 0.1, 100.0)  # general

    view = Espai.view(0.0, 0.0, -4.0)  # 1 / tipus figura

    Cub.view_proj_cub(cub_shader, view, proj)

    cube_positions = [(2.0, 5.0, -15.0), (-1.5, -1.2, -2.5), (1.0, -0.0, -4.0)]

    Finestra.color_fons(0.7, 0.7, 0.7)
    glEnable(GL_DEPTH_TEST)  # profunditat

    while not glfw.window_should_close(window):

        Finestra.events()

        for i in range(len(cube_positions)):
            model = Espai.model(cube_positions[i])
            Espai.model_loc(cub_shader, model)
            glDrawElements(GL_TRIANGLES, cub.indexs.size, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    Render.render_to_jpg()
    glfw.terminate()


if __name__ == "__main__":
    main()
