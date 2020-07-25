from setuptools import setup


setup(
    name='ot2_protocol_generator',
    url='https://github.com/olichen/ot2_protocol_generator',
    version='1.0',
    author='Oliver Chen',
    author_email='olichen@ucdavis.edu',
    description='Opentrons protocol generator for Eton Bioscience Inc.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['ot2_protocol_generator'],
)
