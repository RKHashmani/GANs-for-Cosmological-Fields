#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-B --name Mcdm-B_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose &&

python train.py --dataroot ./datasets/IllustrisTNG/HI-B --name HI-B_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose