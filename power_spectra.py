# calculate power spectra, bispectra, cross correlation, cosmic variance

import numpy as np
import matplotlib.pyplot as plt
import Pk_library as PKL

grid              = 250    #grid size
BoxSize           = 25      #Mpc/h
seed              = 1      #value of the initial random seed
Rayleigh_sampling = 1      #whether sampling the Rayleigh distribution for modes amplitudes
threads           = 1      #number of openmp threads
verbose           = True   #whether to print some information

def get_pk(dataset_type = "Mcdm-HI_CUT", curr_type = 'real_B', initial = 9000, filename = 'dm'):

    MAS = 'None'

    file_1 = f'./results/{dataset_type}/test_latest/images/{curr_type}/{filename}_{initial}.npy'
    curr_map = np.load(file_1)

    # compute the overdensity map
    overdensity_map = curr_map / np.mean(curr_map, dtype=np.float64)
    overdensity_map -= 1.0

    # compute the power spectrum
    Pk2D = PKL.Pk_plane(overdensity_map.astype(np.float32), BoxSize, MAS, threads, verbose=False)

    # get the attributes of the routine
    k = Pk2D.k  # k in h/Mpc
    Pk = Pk2D.Pk  # Pk in (Mpc/h)^2

    # initialize list to hold all power spectrums
    master_Pk = [[Pk]]

    for i in range(9001, 12000):
        # for i in range(1, 15*realizations):

        file = f'./results/{dataset_type}/test_latest/images/{curr_type}/{filename}_{i}.npy'
        curr_map = np.load(file)

        # compute the overdensity map
        overdensity_map = curr_map / np.mean(curr_map, dtype=np.float64)
        overdensity_map -= 1.0

        Pk2D = PKL.Pk_plane(overdensity_map.astype(np.float32), BoxSize, MAS, threads, verbose=False)

        # get the attributes of the routine
        Pk = Pk2D.Pk  # Pk in (Mpc/h)^2

        master_Pk += [[Pk]]

    [Pk_avg] = np.average(master_Pk, axis=0)
    [Pk_std] = np.std(master_Pk, axis=0)

    # np.save('stats/Pk/'+curr_type+'_Pk.npy', Pk_avg)
    # np.save('stats/Pk/'+curr_type+'_Pk_std.npy', Pk_std)
    # np.save('stats/Pk/'+curr_type+'_Pk_k.npy', k)

    plt.plot(k, Pk_avg, label = curr_type)
    plt.fill_between(k, Pk_avg - Pk_std, Pk_avg + Pk_std, alpha=0.2)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel('k')
    plt.ylabel(r'$P(k) [({\rm Mpc}/h)^2]$')
    plt.legend()



# get_pk(dataset_type = "Mcdm-HI_CUT", curr_type = 'fake_B', initial = 9000)
# get_pk(dataset_type = "Mcdm-HI_CUT", curr_type = 'real_B', initial = 9000)
# plt.show()

get_pk(dataset_type = "Mcdm-B_CUT", curr_type = 'fake_B', initial = 9000)
get_pk(dataset_type = "Mcdm-B_CUT", curr_type = 'real_B', initial = 9000)
plt.show()
#
# get_pk(dataset_type = "HI-B_CUT", curr_type = 'fake_B', initial = 9000, filename = 'nh')
# get_pk(dataset_type = "HI-B_CUT", curr_type = 'real_B', initial = 9000, filename = 'nh')
# plt.show()