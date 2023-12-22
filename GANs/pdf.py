import glob
import numpy as np
import Pk_library as PKL
import matplotlib.pyplot as plt


def get_pdf(file_name, label_str, curr_range):
    master_hist = []

    for file in glob.glob(file_name + "*"):
        curr_map = np.load(file)

        hist, bins = np.histogram(np.log10(curr_map).flatten(order='C'), range=curr_range, bins=500, density=True)
        master_hist += [[hist]]

    [avg] = np.average(master_hist, axis=0)
    [std] = np.std(master_hist, axis=0)

    # np.save('stats/pdf/'+curr_type+'_pdf.npy', avg)
    # np.save('stats/pdf/'+curr_type+'_pdf_std.npy', std)
    # np.save('stats/pdf/'+curr_type+'_pdf_bins.npy', bins1)

    plt.plot(bins[:-1], avg, label=label_str)
    plt.fill_between(bins[:-1], avg - std, avg + std, alpha=0.2)
    plt.legend()


get_pdf('./results/HI-B_CUT_Norm/test_latest/images/fake_B/', label_str='Generated', curr_range=(-15, 0))
get_pdf('./results/HI-B_CUT_Norm/test_latest/images/real_B/', label_str='Real', curr_range=(-15, 0))
# get_pdf('HI-B_CUT_Norm/test_latest/images/real_A/', label_str = 'real', curr_range = (0,15))


# x_str = 'log$_{10}\Sigma_{Mcdm}~[M_{\odot}h^{-1}(h^{-1}Mpc)^{-2}]$'   # for Mcdm
# x_str = 'log$_{10}\Sigma_{HI}~[M_{\odot}h^{-1}(h^{-1}Mpc)^{-2}]$'  # for nh
x_str = 'log$_{10}\Sigma_{B}~[M_{\odot}h^{-1}(h^{-1}Mpc)^{-2}]$'   # for B
plt.title('PDF HI-B')
plt.xlabel(x_str)
plt.ylabel('Density')
plt.yscale('log')
plt.savefig("./results/plots/pdf_HI-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

#######################

get_pdf('./results/Mcdm-B_CUT_Norm/test_latest/images/fake_B/', label_str='Generated', curr_range=(-15, 0))
get_pdf('./results/Mcdm-B_CUT_Norm/test_latest/images/real_B/', label_str='Real', curr_range=(-15, 0))

x_str = 'log$_{10}\Sigma_{B}~[M_{\odot}h^{-1}(h^{-1}Mpc)^{-2}]$'   # for B
plt.title('PDF Mcdm-B')
plt.xlabel(x_str)
plt.ylabel('Density')
plt.yscale('log')
plt.savefig("./results/plots/pdf_Mcdm-B.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

#######################

get_pdf('./results/Mcdm-HI_CUT_Norm/test_latest/images/fake_B/', label_str='Generated', curr_range=(0, 10))
get_pdf('./results/Mcdm-HI_CUT_Norm/test_latest/images/real_B/', label_str='Real', curr_range=(0, 10))

x_str = 'log$_{10}\Sigma_{HI}~[M_{\odot}h^{-1}(h^{-1}Mpc)^{-2}]$'  # for HI
plt.title('PDF Mcdm-HI')
plt.xlabel(x_str)
plt.ylabel('Density')
plt.yscale('log')
plt.savefig("./results/plots/pdf_Mcdm-HI.pdf", dpi=600, facecolor="white", edgecolor='none', bbox_inches="tight")
plt.show()
plt.clf()

#######################