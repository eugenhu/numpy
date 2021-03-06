"""
An enhanced distutils, providing support for Fortran compilers, for BLAS,
LAPACK and other common libraries for numerical computing, and more.

Public submodules are::

    misc_util
    system_info
    cpu_info
    log
    exec_command

For details, please see the *Packaging* and *NumPy Distutils User Guide*
sections of the NumPy Reference Guide.

For configuring the preference for and location of libraries like BLAS and
LAPACK, and for setting include paths and similar build options, please see
``site.cfg.example`` in the root of the NumPy repository or sdist.

"""

# Must import local ccompiler ASAP in order to get
# customized CCompiler.spawn effective.
from . import ccompiler
from . import unixccompiler

from .npy_pkg_config import *


def customized_fcompiler(plat=None, compiler=None):
    from numpy.distutils.fcompiler import new_fcompiler
    c = new_fcompiler(plat=plat, compiler=compiler)
    c.customize()
    return c

def customized_ccompiler(plat=None, compiler=None, verbose=1):
    c = ccompiler.new_compiler(plat=plat, compiler=compiler, verbose=verbose)
    c.customize('')
    return c
