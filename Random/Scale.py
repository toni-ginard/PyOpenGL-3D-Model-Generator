#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Scale:

    @staticmethod
    def get_random_scale():
        scale = []
        for i in range(3):
            scale.append(round(random.uniform(0.4, 1.5), 1))
        return scale
