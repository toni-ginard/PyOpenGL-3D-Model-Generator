from OpenGL.GL import *
import os
from PIL import Image


def render_to_jpg(img_name, path):
    """ Renders an image and stores it in the specified path.

    :param img_name: image's name to be stored.
    :param path: path where to store the image.
    """
    # os.chdir("/Users/toniginard/PycharmProjects/Generador-Models-3D/res/img")
    os.chdir(path)
    x, y, width, height = glGetDoublev(GL_VIEWPORT)
    width, height = int(width), int(height)
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(x, y, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(img_name, "JPEG")
    # os.chdir("/Users/toniginard/PycharmProjects/Generador-Models-3D")
    # os.chdir("/Users/toniginard/Desktop/TFG/Images/TrainSet/")
