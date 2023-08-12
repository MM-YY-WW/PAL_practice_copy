from setuptools import setup, find_packages
setup(name='pal',
      version='0.1',
      description='PAL',
      packages=['pal', 'pal_core', 'pal.prompt'],
      install_requires=['openai', 'python-dateutil'])

# this file is used to pack the module into package, 
# therefore could be installed by tools like pip
#



