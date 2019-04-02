#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Position:

    @staticmethod
    def get_random_position():
        z = random.randrange(-10, 0, 1)
        x = random.randrange(z - 5, -z + 5, 1)
        y = random.randrange(z - 5, -z + 5, 1)
        posicio = [float(x), float(y), float(z)]
        return posicio

    @staticmethod
    def array_posicions(mida):
        posicions = []
        for i in range(0, mida):
            posicions.append(Position.get_random_position())

        return posicions