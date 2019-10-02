#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def get_random_rotation():
    """ Generates random rotation, in degrees.
    :return: axis degrees.
    """
    return random.randrange(0, 90, 1)
