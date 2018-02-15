# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Setuptools is needed to install all dependencies")
    print("Setuptools: https://pypi.python.org/pypi/setuptools")

import platform
import os

if not platform.system() == "Linux":
    print("Warning: Uncertainpy not tested for current operating system")

name = "uncertainpy"

uncertainpy_req = ["xvfbwrapper", "chaospy", "tqdm", "h5py",
                   "multiprocess", "numpy", "scipy", "seaborn", "matplotlib"]

extras_require = {
    'spike_features':  ["efel"],
    'network_features': ["elephant", "neo", "quantities"],
}

all_requires = ["xvfbwrapper", "chaospy", "tqdm", "h5py",
                "multiprocess", "numpy", "scipy", "seaborn",
                "efel", "elephant",  "neo", "quantities", "matplotlib"]

long_description = open("README.md").read()

# Remove badges from the description
long_description = "\n".join(long_description.split("\n")[4:])

with open("VERSION") as version_file:
    version = version_file.read().strip()

packages = ['uncertainpy', 'uncertainpy.models', 'uncertainpy.features', 'uncertainpy.plotting', 'uncertainpy.utils']
setup(name=name,
      version=version,
    #   url="https://github.com/simetenn/uncertainpy",
    #   author="Simen Tennøe",
    #   description='Uncertainty quantification and sensitivity analysis',
    #   long_description=long_description,
      python_requires="==2.7",
      packages=find_packages("src"),
      package_dir={"": "src"},
      data_files=["README.md", "VERSION"],
      install_requires=all_requires,
      extras_require=extras_require,
      )
