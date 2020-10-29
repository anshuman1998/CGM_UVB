# A simple code to run cloudy and store its output

import os
import numpy as np
import subprocess


def run(cloudy_path, input_file):
    """
    :param cloudy_path: the path where your cloudy files are stored
    :param input_file: the input file (with full path) to run
    :return:
    """
    # find the original path
    basepath = os.getcwd()

    # go to the directory of input file
    os.chdir(os.path.dirname(input_file))

    # input file name
    file_name = os.path.basename(input_file)

    run_command =  cloudy_path + '/source/cloudy.exe'
    process = subprocess.Popen([run_command, file_name], stdout=subprocess.PIPE)
    process.stdout.read()

    # come back to the original path
    os.chdir(basepath)

    return


def write_input(file_name, *args, **kwargs):

    f = open(file_name, "w+")

    if kwargs['uvb'] == 'KS18':
        uvb_statement =  'TABLE {} redshift = {} [scale = {}] [Q = {}] \n'.format(
            kwargs['z'], kwargs['uvb'], kwargs['uvb_scale'], kwargs['uvb_Q'])
        f.write(uvb_statement)

    density_statement= 'hden {} \n'.format(kwargs['log_hden'])
    if kwargs['hden_vary'] == True:
        density_statement= 'hden {} vary \n'.format(kwargs['log_hden'])
        variation_statement = 'grid range from {} to {} with {} dex step \n'.format(
            kwargs['log_hden1'], kwargs['log_hden2'], kwargs['log_hden_step'])
        f.write(density_statement)
        f.write(variation_statement)
    else:
        f.write(density_statement)

    metal_statement =  'metals {:.2f} log \n'.format(kwargs['log_metal'])
    f.write(metal_statement)

    if 'scale_He' in kwargs.keys():
        scale_He_statement ='element helium abundance {} linear \n'.format(kwargs['scale_He'])
        f.write(scale_He_statement)

    stop_statement = 'stop column density {}  neutral H \n'.format(kwargs['stop_logNHI'])
    f.write(stop_statement)

    if 'constant_T' in kwargs.keys():
        temp_statement =  'constant temperature, t={} K [linear] \n'.format(kwargs['constant_T'])
        f.write(temp_statement)

    if 'out_file_ext' in kwargs.keys():
        out_file_extension = kwargs['out_file_ext']
    else:
        out_file_extension = '.spC'

    save_statement = 'save species column density {} no hash \n'.format(out_file_extension)
    f.write(save_statement)

    for ion in args:
        write_ion = "\"{}\" \n".format(ion)
        f.write(write_ion)

    f.write('end')

    f.close()

    return


# this is the part one needs to change if one wants to change the cloudy program
def cloudy_params_defaults(z=0.2, T = 10000, metal = -1, stop_NHI = 14):
    default_things ={}
    


    return ions, default_things

"""
UVB_Q = 20
dirname = '/home/vikram/cloudy_run/final'
run = '/home/vikram/c17.02/source/cloudy.exe'
hden = np.arange(-5, -2.999, 1)  # Hydrogen density grid
z = -1  # in log scale
stcolden = 14
if not os.path.exists(dirname):
    os.makedirs(dirname)

os.chdir(dirname)

filena = dirname + '/prog' + '{:.0f}'.format(UVB_Q) + '_Oct5.in'
f = open(filena, "w+")
f.write("TABLE KS18 redshift = 0.2 [scale= 1][Q=" + "{:.0f}".format(UVB_Q)
        + "] \nhden -4 vary \ngrid range from -5 to -3 with 1 dex steps \nmetals "
        + "{:.2f}".format(z) + " log \nelement helium abundance 0.081632653 linear \nstop column density "
        + "{:.1f}".format(
    stcolden) + " neutral H \nconstant temperature, t=1e4 K [linear] \nsave species column density \".spC\" no hash \n\"C+\" \n\"C+2\" \n\"C+3\" \n\"N+\" \n\"N+2\" \n\"N+3\" \n\"N+4\" \n\"O\" \n\"O+\"  \n\"O+2\" \n\"O+3\" \n\"O+4\" \n\"O+5\" \n\"S+3\" \n\"S+4\" \n\"S+5\" \n\"Si+\" \n\"Si+2\" \n\"Si+3\" \nend")
f.close()
process = subprocess.Popen([run, "prog" + "{:.0f}".format(UVB_Q) + "_Oct5.in"],
                           stdout=subprocess.PIPE)
process.stdout.read()

outfilename = filena.split('.in')[0] + '.spC'
data_20 = np.genfromtxt(outfilename)


print("Done!!")
"""
