#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Color:

    @staticmethod
    def get_random_color():
        color = []
        for i in range(3):
            color.append(round(random.uniform(0.4, 1.0), 1))
        return color

    @staticmethod
    def get_background_color():
        color = []
        channel = round(random.uniform(0.6, 1.0), 1)
        for i in range(3):
            color.append(channel)
        return color
