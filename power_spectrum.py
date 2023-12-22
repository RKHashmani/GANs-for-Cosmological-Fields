import glob
import numpy as np
import Pk_library as PKL
import matplotlib.pyplot as plt

grid = 250  # grid size
BoxSize = 25  # Mpc/h
seed = 1  # value of the initial random seed
Rayleigh_sampling = 1  # whether sampling the Rayleigh distribution for modes amplitudes
threads = 1  # number of openmp threads
verbose = True  # whether to print some information


# calculate power spectra, bispectra, cross correlation, cosmic variance
def get_pk(file_name, label_str):
    MAS = 'None'

    # initialize list to hold all power spectrums
    master_Pk = []

    # for i in range(9001, 12000):
    for name in glob.glob(file_name + "*"):
        # print(name)

        # file = f'./results/{dataset_type}/test_latest/images/{curr_type}/{filename}_{i}.npy'
        curr_map = np.load(name)

        # compute the overdensity map
        overdensity_map = curr_map / np.mean(curr_map, dtype=np.float64)
        overdensity_map -= 1.0

        Pk2D = PKL.Pk_plane(overdensity_map.astype(np.float32), BoxSize, MAS, threads, verbose=False)

        # get the attributes of the routine
        Pk = Pk2D.Pk  # Pk in (Mpc/h)^2
        k = Pk2D.k  # k in h/Mpc

        master_Pk += [[Pk]]

    [Pk_avg] = np.average(master_Pk, axis=0)
    [Pk_std] = np.std(master_Pk, axis=0)
    # print(Pk_avg)
    # print(Pk_std)

    plt.plot(k, Pk_avg, label=label_str)
    plt.fill_between(k, Pk_avg - Pk_std, Pk_avg + Pk_std, alpha=0.2)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel('k $[h/Mpc]$')
    plt.ylabel(r'$P(k) [(Mpc/h)^2]$')
    plt.legend()


get_pk('./results/HI-B_CUT_Norm/test_latest/images/fake_B/', label_str='Generated')
get_pk('./results/HI-B_CUT_Norm/test_latest/images/real_B/', label_str='Real')
plt.title('Power Spectrum HI-B')
plt.savefig("./results/plots/Power_Spectrum_HI-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

get_pk('./results/Mcdm-HI_CUT_Norm/test_latest/images/fake_B/', label_str='Generated')
get_pk('./results/Mcdm-HI_CUT_Norm/test_latest/images/real_B/', label_str='Real')
plt.title('Power Spectrum Mcdm-HI')
plt.savefig("./results/plots/Power_Spectrum_Mcdm-HI.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

get_pk('./results/Mcdm-B_CUT_Norm/test_latest/images/fake_B/', label_str='Generated')
get_pk('./results/Mcdm-B_CUT_Norm/test_latest/images/real_B/', label_str='Real')
plt.title('Power Spectrum Mcdm-B')
plt.savefig("./results/plots/Power_Spectrum_Mcdm-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()