#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Position:

    @staticmethod
    def get_posicio():
        z = random.randrange(-10, 0, 1)
        x = random.randrange(z - 5, -z + 5, 1)
        y = random.randrange(z - 5, -z + 5, 1)
        posicio = [float(x), float(y), float(z)]
        return posicio

