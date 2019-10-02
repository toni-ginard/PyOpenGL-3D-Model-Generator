#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def get_random_scale():
    """ Generates random scaling vector.
    :rtype numpy.array
    :return: scaling vector.
    """
    scale = []
    for i in range(3):
        scale.append(round(random.uniform(0.2, 3.0), 1))
    return scale
