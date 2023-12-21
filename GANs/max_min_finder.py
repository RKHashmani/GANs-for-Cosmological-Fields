import numpy as np
import glob


def get_max_min(dataset="Mcdm-HI", phase="trainA", filename="dm"):
    max_value = float('-inf')
    min_value = float('inf')

    npfiles = glob.glob(f'./datasets/IllustrisTNG/{dataset}/{phase}/{filename}_*.npy')
    npfiles.sort()
    all_arrays = []
    for npfile in npfiles:
        all_arrays.append(np.load(npfile))
    all_arrays = np.array(all_arrays)
    Amin = all_arrays.min()
    Amax = all_arrays.max()
    scaledA = (all_arrays - Amin) / (Amax - Amin)
    normA = (scaledA - scaledA.mean()) / scaledA.std()
    print(f"The new mean and std is {normA.mean()}, {normA.std()}")
    return all_arrays.max(), all_arrays.min(), all_arrays.mean(), all_arrays.std(), scaledA.mean(), scaledA.std()

Mcdm_max, Mcdm_min, Mcdm_mean, Mcdm_std, scaledA_mean, scaledA_std = get_max_min(dataset="Mcdm-HI", phase="trainA", filename="dm")
print(f"Mcdm max value is {Mcdm_max}")
print(f"Mcdm min value is {Mcdm_min}")
# print(f"Mcdm mean value is {Mcdm_mean}")
# print(f"Mcdm std value is {Mcdm_std}")
print(f"Mcdm scaled mean value is {scaledA_mean}")
print(f"Mcdm scaled std value is {scaledA_std}")

HI_max, HI_min, HI_mean, HI_std, scaledB_mean, scaledB_std = get_max_min(dataset="Mcdm-HI", phase="trainB", filename="nh")
print(f"HI max value is {HI_max}")
print(f"HI min value is {HI_min}")
# print(f"HI mean value is {HI_mean}")
# print(f"HI std value is {HI_std}")
print(f"HI scaled mean value is {scaledB_mean}")
print(f"HI scaled std value is {scaledB_std}")

B_max, B_min, B_mean, B_std, scaledB_mean, scaledB_std = get_max_min(dataset="Mcdm-B", phase="trainB", filename="B")
print(f"B max value is {B_max}")
print(f"B min value is {B_min}")
# print(f"B mean value is {B_mean}")
# print(f"B std value is {B_std}")
print(f"B scaled mean value is {scaledB_mean}")
print(f"B scaled std value is {scaledB_std}")
