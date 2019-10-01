#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Model import *


NUM_MODELS = 100000
IMG_INICIAL = 0
MAIN_PATH = ""
SET = "/Train"


if __name__ == "__main__":

    create_model("/Volumes/TONI32/Prova/Train",
                 num_models=2,
                 img_inicial=0,
                 img_size=32)

