import numpy as np
import pybind11
from setuptools import Extension, setup

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'ccocotools._mask',
        sources=['ccocotools/common/maskApi.c', 'ccocotools/_mask.pyx'],
        include_dirs=[np.get_include(), 'ccocotools/common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99', '-Wno-misleading-indentation'],
    ),
    Extension(
        'ccocotools._fastcoco',
        sources=['ccocotools/csrc/vision.cpp', 'ccocotools/csrc/cocoeval/cocoeval.cpp'],
        include_dirs=[np.get_include(), pybind11.get_include(), 'ccocotools/csrc'],
        extra_compile_args=['-O3'],
        language='c++'
    )
]

setup(
    name='ccocotools',
    packages=['ccocotools'],
    package_dir={'ccocotools': 'ccocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='1.0',
    ext_modules=ext_modules
)
