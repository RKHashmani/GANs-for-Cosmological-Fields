# Generative Mapping Between Fields in the IllustrisTNG Dataset

For our Computational Cosmology course project, we build a bijective mapping between physical fields from the CAMELS simulation using a state-of-the-art GAN specializing in unpaired image-to-image translation.

We train a Contrastive Unpaired Translation (CUT) model to create these mappings between dark matter and neutral hydrogen (Mcdm-HI), dark matter and magnetic fields magnitude (Mcdm-B), and neutral hydrogen and magnetic fields magnitude (HI-B). We then evaluate the performance of our models using 3 summary statistics: the power spectrum, cross correlation coefficient, and the probability distribution function.

## Instructions
Note: Both the CUT and CycleGAN models are implemented for this project.
### 1. Installation
``` conda env create -f environment.yml ```

### 2. Usage
#### Training
``` python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 4.57e14 --Amin 6.097e10 --A_scaled_mean 6.55e-4 --A_scaled_std 5.64e-4 --Bmax 5.34e11 --Bmin 6.17e5 --B_scaled_mean 2.11e-4 --B_scaled_std 1.74e-3 --verbose --n_epochs 100 --n_epochs_decay 0 && ```

#### Testing
``` python test.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --min_max_scale --standardize --Amax 4.57e14 --Amin 6.097e10 --A_scaled_mean 6.55e-4 --A_scaled_std 5.64e-4 --Bmax 5.34e11 --Bmin 6.17e5 --B_scaled_mean 2.11e-4 --B_scaled_std 1.74e-3 --eval --verbose --phase test --num_test 3000 ```