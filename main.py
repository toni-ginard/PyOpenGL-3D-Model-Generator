#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Model import *


NUM_MODELS = 2
IMG_INICIAL = 0
MAIN_PATH = ""
SET = "/Train"


if __name__ == "__main__":

    create_model("/Users/toniginard/Desktop/Img_Prova/Train",
                 num_models=2,
                 initial_model=0,
                 img_size=64)

