#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Color:

    @staticmethod
    def get_random_color():
        color = []
        for i in range(3):
            color.append(round(random.uniform(0.0, 1.0), 1))
        return color
