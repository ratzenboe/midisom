#!/usr/bin/env python

from distutils.core import setup

setup(name='Midisom',
  version= '1.0',
  description='Extensions to the Minisom package including status bars and plotting routines',
  author='Sebastian Ratzenböck',
  package_data={'': ['Readme.md']},
  include_package_data=True,
  license="CC BY 3.0",
  py_modules=['midisom'],
  requires = ['pandas','tqdm','matplotlib','numpy'],
  url = 'https://github.com/ratzenboe/midisom',
  keywords = ['machine learning', 'neural networks', 'clustering', 'dimentionality reduction']
 )
