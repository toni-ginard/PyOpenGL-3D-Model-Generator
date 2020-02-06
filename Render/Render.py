#!/usr/bin/env python
# -*- coding: utf-8 -*-


from OpenGL.GL import *
from PIL import Image
import os


def render_to_jpg(path):
    """ Renders an image and stores it in the specified path.

    :param path: path where to store the image.
    """
    # print(os.getcwd() + ' - ' + path)
    x, y, width, height = glGetDoublev(GL_VIEWPORT)
    width, height = int(width), int(height)
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(x, y, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(os.getcwd() + path, "JPEG")
