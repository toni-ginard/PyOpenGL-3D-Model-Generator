#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Rotation:

    @staticmethod
    def get_random_rotation():
        return random.randrange(0, 90, 1)
