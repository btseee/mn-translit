# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
try:
    with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = ''

# Get version from __init__.py
version = {}
with open(os.path.join(here, 'src', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, version)
            break

setup(
    name='mn-translit',
    version=version.get('__version__', '1.0.0'),
    description='Mongolian Latin-Cyrillic transliteration library following MNS 5217:2012 standard',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    # Author information
    author='Battseren Badral',
    author_email='bbattseren88@gmail.com',

    # Project URLs
    url='https://github.com/btseee/mn-translit',
    project_urls={
        'Bug Reports': 'https://github.com/btseee/mn-translit/issues',
        'Source': 'https://github.com/btseee/mn-translit',
    },
    
    # License
    license='MIT',
    
    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        
        # Python version support
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    
    # Keywords
    keywords='mongolian transliteration cyrillic latin mns-5217 translation',
    
    # Package configuration
    packages=find_packages(exclude=['tests', 'examples']),
    
    # Python version requirement
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    
    # Dependencies (none required for basic functionality)
    install_requires=[],
    
    # Optional dependencies
    extras_require={
        'dev': ['pytest>=3.0', 'pytest-cov'],
        'test': ['pytest>=3.0', 'pytest-cov'],
    },
    
    # Include package data
    include_package_data=True,
    
    # Zip safe
    zip_safe=False,
)
