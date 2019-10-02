#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def get_random_color():
    """ Generates rgb color.
    :rtype numpy.array
    :return: rbg color.
    """
    color = []
    for i in range(3):
        color.append(round(random.uniform(0.4, 1.0), 1))
    return color


def get_background_color():
    """ Generates random soft color for the background.
    :rtype numpy.array
    :return: rbg color.
    """
    color = []
    channel = round(random.uniform(0.6, 1.0), 1)
    for i in range(3):
        color.append(channel)
    return color
