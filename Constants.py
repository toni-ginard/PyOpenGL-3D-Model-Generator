#!/usr/bin/env python
# -*- coding: utf-8 -*-


# nº figures
MIN_CUBS = 5
MAX_CUBS = 10
MIN_PIRS = 5
MAX_PIRS = 10

# PATHS
DEPTH_PAHT = "/depth/depth/"
LEFT_PATH = "/left/left/"
RIGHT_PATH = "/right/right/"

# SHADERS
VERTEX_SHADER = "Shaders/vertex_shader.vs"
FRAGMENT_SHADER = "Shaders/fragment_shader.fs"
DEPTH_FRAGMENT_SHADER = "Shaders/depth_fragment_shader.fs"

# CAMERAS
CENTER = [0.0, 0.0, 5.0]
CENTER_TARGET = [0.0, 0.0, 0.0]
CENTER_CAMERA = [CENTER, CENTER_TARGET]

LEFT = [-0.05, 0.0, 5.0]
LEFT_TARGET = [-0.05, 0.0, 0.0]
LEFT_CAMERA = [LEFT, LEFT_TARGET]

RIGHT = [0.05, 0.0, 5.0]
RIGHT_TARGET = [0.05, 0.0, 0.0]
RIGHT_CAMERA = [RIGHT, RIGHT_TARGET]
