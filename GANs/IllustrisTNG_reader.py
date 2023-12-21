'''
To visualize NumPy files from IllustrisTNG
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

file_name1 = "dm_9000.npy"
file_name2 = "nh_9000.npy"

# Load the data
Mcdm = np.load(f'./datasets/IllustrisTNG/Mcdm-HI/testA/{file_name1}')
HI = np.load(f'./datasets/IllustrisTNG/Mcdm-HI/testB/{file_name2}')

real_A = np.load(f'./results/Mcdm-HI_CUT/test_latest/images/real_A/{file_name1}')
real_B = np.load(f'./results/Mcdm-HI_CUT/test_latest/images/real_B/{file_name1}')
fake_B = np.load(f'./results/Mcdm-HI_CUT/test_latest/images/fake_B/{file_name1}')

fake_B = (fake_B - fake_B.min()) / (fake_B.max() - fake_B.min())

# Mcdm = np.pad(Mcdm, [(1, 1), (1, 1)], 'constant')



# print(f"Are the Mcdm and real_A matrices the same: {np.isclose(Mcdm, real_A).all()}")
# print(f"Are the HI and real_B matrices the same: {np.isclose(HI, real_B).all()}")
# print (real_A[-1,240:])
# print (Mcdm[-1,240:])

# if np.isclose(Mcdm, real_A).all():
#     print("Numpy Matrices are the same")
# else:
#     print("Numpy Matrices are not the same")

fig , ((ax1,ax2) , (ax3,ax4), (ax5,ax6)) = plt.subplots(3, 2, figsize=(12, 12))
fig.tight_layout()

z1_plot = ax1.imshow(Mcdm, origin='lower',interpolation='bicubic',norm = LogNorm())
ax1.set_title('Mcdm')
plt.colorbar(z1_plot,ax=ax1)

z2_plot = ax2.imshow(real_A, origin='lower',interpolation='bicubic',norm = LogNorm())
ax2.set_title('real_A')
plt.colorbar(z2_plot,ax=ax2)

z3_plot = ax3.imshow(HI,origin='lower',interpolation='bicubic',norm = LogNorm())
ax3.set_title('HI')
plt.colorbar(z3_plot,ax=ax3)

z4_plot = ax4.imshow(real_B,origin='lower',interpolation='bicubic',norm = LogNorm())
ax4.set_title('real_B')
plt.colorbar(z4_plot,ax=ax4)

z5_plot = ax5.imshow(Mcdm, origin='lower',interpolation='bicubic',norm = LogNorm())
ax5.set_title('Mcdm (Same as Above)')
plt.colorbar(z5_plot,ax=ax5)

z6_plot = ax6.imshow(fake_B,origin='lower',interpolation='bicubic',norm = LogNorm())
ax6.set_title('fake_B')
plt.colorbar(z6_plot,ax=ax6)


plt.show()



print("done!")