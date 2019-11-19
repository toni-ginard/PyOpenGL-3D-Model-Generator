#!/usr/bin/env python
# -*- coding: utf-8 -*-


# nº figures
NUM_CUBES = 15
NUM_PYRAMIDS = 15

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
