'''
To visualize NumPy files from IllustrisTNG
'''

import numpy as np
# import matplotlib.pyplot as plt

# Load the data
data = np.load('./datasets/IllustrisTNG/Mcdm-HI/trainA/dm_0.npy')
data2 = np.load('./datasets/IllustrisTNG/Mcdm-HI/trainB/nh_0.npy')

print("done.")