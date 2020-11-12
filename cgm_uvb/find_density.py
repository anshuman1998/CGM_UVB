import numpy as np
import astropy.table as tab


def get_true_model(model ='/home/vikram/cloudy_run/anshuman/try_Q18.fits'):
    """
    :param model: The data where Q18 model is stored
    :return: a row of ion column densities at n_H = 1e-4 cm^-2
    """
    data = tab.Table.read(model)
    true_ion_col = data [data['hden'] == 1e-4]

    return true_ion_col

def find_density_LSF(model_Q, *ions_to_use):
    model = tab.Table.read(model_Q)
    obs_ion_col = get_true_model()

    # filter to use specific ions
    least_square_array = np.zeros(len(model))
    hden_array = np.array(model['hden'])
    for ion in ions_to_use:
        least_square_array += (model[ion] - obs_ion_col[ion])**2

    print(np.min(least_square_array))
    print(hden_array[np.argmin(least_square_array)])

    return  hden_array, least_square_array

model ='/home/vikram/cloudy_run/anshuman/try_Q14.fits'
ions= ['C+3', 'C+2', 'Si+3', 'Si+2', 'O+5']

find_density_LSF(model, *ions)




"""
    ions = ["H", "H+",
            "He", "He+", "He+2",
            "C", "C+", "C+2", "C+3", "C+4", "C+5",
            "N", "N+", "N+2", "N+3", "N+4",
            "O", "O+", "O+2", "O+3", "O+4", "O+5", "O+6", "O+7",
            "S", "S+", "S+2", "S+3", "S+4", "S+5",
            "Si", "Si+", "Si+2", "Si+3", "Si+4"]
"""




