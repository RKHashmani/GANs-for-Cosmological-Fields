'''
To visualize NumPy files from IllustrisTNG
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

file_name1 = "dm_9000.npy"
file_name2 = "nh_9000.npy"



real_A = np.load(f'./results/Mcdm-HI_CUT/test_latest/images/real_A/{file_name1}')

# fig = plt.figure()
# ax = fig.add_subplot(111)

plt.imshow(real_A, origin='lower',interpolation='bicubic',norm = LogNorm())
plt.title('real_A')
plt.colorbar()
plt.tight_layout()


plt.savefig("Test.png", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")

plt.show()



print("done!")