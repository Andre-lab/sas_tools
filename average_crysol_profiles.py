"""
Averaging crysol profiles read from files
"""

import os
import glob
import numpy as np


def read_file_safe(filename, dtype="float64"):
    """
    Simple check if file exists
    :param filename:
    :return:
    """
    try:
        results = np.genfromtxt(filename, dtype=dtype, skip_header=1)
    except IOError as err:
        print(os.strerror(err.errno))
    return results

if __name__ == "__main__":

    doc = """
        Averages crysol files from *int files in the current directory  
        """
    print(doc)

    combined_intensity = []
    combined_errors = []
    crysol_files = glob.glob('*00.int')
    for crysol_file in crysol_files:
        experimental = read_file_safe(crysol_file)
        qvector = experimental[:,0]
        intensity = experimental[:,1]
        errors = experimental[:,2]
        combined_intensity.append(intensity)
        combined_errors.append(errors)
    combined_intensity = np.average(combined_intensity, axis=0)
    combined_errors = np.average(combined_errors, axis=0)
    np.savetxt('combined_profile.dat',
           np.transpose([qvector, combined_intensity]))

