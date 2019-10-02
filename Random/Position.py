#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def get_random_position():
    """ Generates a randomposition in world coordinates.
    :rtype numpy.array.
    :return: world coordinates.
    """
    z = random.randrange(-10, 0, 1)
    x = random.randrange(z - 4, -z + 4, 1)
    y = random.randrange(z - 4, -z + 4, 1)
    position = [float(x), float(y), float(z)]
    return position
