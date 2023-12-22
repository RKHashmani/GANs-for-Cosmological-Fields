import glob
import numpy as np
import Pk_library as PKL
import matplotlib.pyplot as plt


# calculate power spectra, bispectra, cross correlation, cosmic variance
def get_cross_corr(file_name1, file_name2, label_str):
    MAS = 'None'
    BoxSize = 25  # Mpc/h
    threads = 1  # number of openmp threads

    # initialize list to hold all power spectrums
    master_r = []

    for file_1 in glob.glob(file_name1 + "*"):
        last_str = file_1.split('_')[-1]
        num = int(last_str.split('.')[0])

        [file_2] = glob.glob(file_name2 + '*' + str(num) + '.*')

        map1 = np.load(file_1)
        map2 = np.load(file_2)

        # compute the overdensity map
        delta1 = map1 / np.mean(map1, dtype=np.float64)
        delta1 -= 1.0

        delta2 = map2 / np.mean(map2, dtype=np.float64)
        delta2 -= 1.0

        XPk2D = PKL.XPk_plane(delta1.astype(np.float32), delta2.astype(np.float32), BoxSize, MAS, MAS, threads)

        # get the attributes of the routine
        k = XPk2D.k  # k in h/Mpc
        r = XPk2D.r  # cross-correlation coefficient

        master_r += [[r]]

    [r_avg] = np.average(master_r, axis=0)
    [r_std] = np.std(master_r, axis=0)

    #     np.save('stats/cross_Pk/'+curr_type1+'_'+curr_type2+'_XPk_k.npy', k)
    #     np.save('stats/cross_Pk/'+curr_type1+'_'+curr_type2+'_r.npy', r_avg)
    #     np.save('stats/cross_Pk/'+curr_type1+'_'+curr_type2+'_r_std.npy', r_std)

    plt.plot(k, r_avg)
    plt.fill_between(k, r_avg - r_std, r_avg + r_std, alpha=0.2)
    plt.xscale("log")
    plt.xlabel('k $[h/Mpc]$')
    plt.ylabel('Cross Correlation Coefficient')
    plt.title(label_str)


folder1 = './results/Mcdm-HI_CUT_Norm/test_latest/images/fake_B/'
folder2 = './results/Mcdm-HI_CUT_Norm/test_latest/images/real_B/'
get_cross_corr(folder2, folder1, 'CCC Real vs. Generated Mcdm-HI')
plt.savefig("./results/plots/CCC_Mcdm-HI.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

folder1 = './results/Mcdm-B_CUT_Norm/test_latest/images/fake_B/'
folder2 = './results/Mcdm-B_CUT_Norm/test_latest/images/real_B/'
get_cross_corr(folder2, folder1, 'CCC Real vs. Generated Mcdm-B')
plt.savefig("./results/plots/CCC_Mcdm-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

folder1 = './results/HI-B_CUT_Norm/test_latest/images/fake_B/'
folder2 = './results/HI-B_CUT_Norm/test_latest/images/real_B/'
get_cross_corr(folder2, folder1, 'CCC Real vs. Generated HI-B')
plt.savefig("./results/plots/CCC_HI-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()