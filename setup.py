import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import setup

setup(
    name='noseprogress',
    #version='0.1',
    author='landhu',
    author_email = 'landhu@hotmail.com',
    description = 'A plugin of progress',
    license = 'landhu',
    entry_points = {
        'nose.plugins': [
            'noseprogress = noseprogress:Progress'
            ]
        }

    )
