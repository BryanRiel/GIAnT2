#-*- coding: utf-8 -*-

import numpy as np
import sys
import os


def configuration(parent_package='', top_path=None):

    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)
    config.set_options(assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('giant')
    config.get_version('giant/version.py')

    return config


if __name__ == '__main__':

    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    # Run build
    from numpy.distutils.core import setup

    try:
        setup(
            name='giant',
            maintainer='Bryan Riel',
            description='GIAnT-2',
            author='Bryan Riel',
            author_email='bryanvriel@gmail.com',
            configuration=configuration)
    finally:
        del sys.path[0]
        os.chdir(old_path)

# end of file
