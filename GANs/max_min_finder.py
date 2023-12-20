import numpy as np
import glob

def get_max_min(dataset="Mcdm-HI", phase="trainA", filename="dm"):
    max_value = float('-inf')
    min_value = float('inf')

    npfiles = glob.glob(f'./datasets/IllustrisTNG/{dataset}/{phase}/{filename}_*.npy')
    npfiles.sort()
    for npfile in npfiles:
        data = np.load(npfile)
        max_value = max(max_value, data.max())
        min_value = min(min_value, data.min())

    return max_value, min_value

Mcdm_max, Mcdm_min = get_max_min(dataset="Mcdm-HI", phase="trainA", filename="dm")
print(f"Mcdm max value is {Mcdm_max}")
print(f"Mcdm min value is {Mcdm_min}")

HI_max, HI_min = get_max_min(dataset="Mcdm-HI", phase="trainB", filename="nh")
print(f"HI max value is {HI_max}")
print(f"HI min value is {HI_min}")

B_max, B_min = get_max_min(dataset="Mcdm-B", phase="trainB", filename="B")
print(f"B max value is {B_max}")
print(f"B min value is {B_min}")
