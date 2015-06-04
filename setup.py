import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'readme.md')) as f:
        README = f.read()

        REQUIREMENTS = []

setup(
    name='raw_input_plus',
    version='0.1',
    description='raw_input_plus',
    author='georgefs',
    author_email='georgefs@gmail.com',
    long_description=README,
    scripts=[],
    url='https://github.com/georgefs/raw_input_plus.git',
    packages=find_packages(),
    license='MIT License',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
