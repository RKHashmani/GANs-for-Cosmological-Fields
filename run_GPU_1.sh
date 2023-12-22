#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-B --name Mcdm-B_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose &&

python train.py --dataroot ./datasets/IllustrisTNG/HI-B --name HI-B_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose


python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 457721779490672.1 --Amin 60970772574.29126 --A_scaled_mean 0.0006551713931004052 --A_scaled_std 0.0005647735866979585 --Bmax 534029910702.803 --Bmin 616794.4824397375 --B_scaled_mean 0.00021139645091832043 --B_scaled_std 0.0017408773268459896 --verbose --n_epochs 100 --n_epochs_decay 0

python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-B --name Mcdm-B_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 457721779490672.1 --Amin 60970772574.29126 --A_scaled_mean 0.0006551713931004052 --A_scaled_std 0.0005647735866979585 --Bmax 22.321495099260055 --Bmin 1.5578756711390206e-09 --B_scaled_mean 2.9568368916918845e-08 --B_scaled_std 7.843592332332748e-05 --verbose --n_epochs 100 --n_epochs_decay 0

python train.py --dataroot ./datasets/IllustrisTNG/HI-B --name HI-B_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 534029910702.803 --Amin 616794.4824397375 --A_scaled_mean 0.00021139645091832043 --A_scaled_std 0.0017408773268459896 --Bmax 22.321495099260055 --Bmin 1.5578756711390206e-09 --B_scaled_mean 2.9568368916918845e-08 --B_scaled_std 7.843592332332748e-05 --verbose --n_epochs 100 --n_epochs_decay 0



python test.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 457721779490672.1 --Amin 60970772574.29126 --A_scaled_mean 0.0006551713931004052 --A_scaled_std 0.0005647735866979585 --Bmax 534029910702.803 --Bmin 616794.4824397375 --B_scaled_mean 0.00021139645091832043 --B_scaled_std 0.0017408773268459896 --eval --verbose --phase test --num_test 3000

python test.py --dataroot ./datasets/IllustrisTNG/Mcdm-B --name Mcdm-B_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 457721779490672.1 --Amin 60970772574.29126 --A_scaled_mean 0.0006551713931004052 --A_scaled_std 0.0005647735866979585 --Bmax 22.321495099260055 --Bmin 1.5578756711390206e-09 --B_scaled_mean 2.9568368916918845e-08 --B_scaled_std 7.843592332332748e-05 --eval --verbose --phase test --num_test 3000

python test.py --dataroot ./datasets/IllustrisTNG/HI-B --name HI-B_CUT_Norm --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 534029910702.803 --Amin 616794.4824397375 --A_scaled_mean 0.00021139645091832043 --A_scaled_std 0.0017408773268459896 --Bmax 22.321495099260055 --Bmin 1.5578756711390206e-09 --B_scaled_mean 2.9568368916918845e-08 --B_scaled_std 7.843592332332748e-05 --eval --verbose --phase test --num_test 3000