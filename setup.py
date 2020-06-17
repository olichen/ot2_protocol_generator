from setuptools import setup
import os

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'ot2_protocol_generator',
    url = 'https://github.com/olichen/ot2_protocol_generator',
    version = '0.1',
    author = 'Oliver Chen',
    author_email = 'olichen@ucdavis.edu',
    description = 'Operntrons protocol generator for Eton Bioscience Inc.',
    long_description = read('README.md'),
    long_description_content_type='text/markdown',
    license = 'MIT',
    packages = ['ot2_protocol_generator'],
)
