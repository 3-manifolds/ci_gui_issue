from setuptools import setup, Extension
from Cython.Build import cythonize

dummy = Extension(
    name = 'snappy_wrap.dummy',
    sources = ['src/snappy_wrap/dummy.pyx'],
)


setup(
    ext_modules = cythonize([dummy]),
)
