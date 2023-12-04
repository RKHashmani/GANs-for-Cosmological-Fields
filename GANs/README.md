# GANs
CycleGAN and CUT models for the field of cosmology.

## 1. Installation
``` conda env create -f environment.yml ```

## 2. Usage
### Training
``` python train.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose ```

### Testing
``` python test.py --dataroot ./datasets/IllustrisTNG/Mcdm-HI --name Mcdm-HI_CUT --model cut --CUT_mode CUT --input_nc 1 --output_nc 1 --verbose ```