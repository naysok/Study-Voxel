from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "calc_color_fast app",
    ext_modules = cythonize('calc_color_fast.pyx'),
    zip_safe = False
)

"""
python setup.py build_ext
# python setup.py install_lib
http://docs.cython.org/en/latest/src/quickstart/build.html
"""