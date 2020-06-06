from setuptools import setup
import os

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'LiquidHandler',
    url = 'https://github.com/olichen/liquidhandler',
    version = '0.1',
    author = 'Oliver Chen',
    author_email = 'olichen@ucdavis.edu',
    description = 'Operntrons protocol generator for Eton Bioscience Inc.',
    long_description = read('README'),
    license = 'MIT',
    packages = ['liquidhandler', 'tests'],
    install_requires = ['opentrons']
)
