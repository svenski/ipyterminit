from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='ipyterminit',
      version='0.1',
      description='Remove ssh ipython setup',
      url='http://github.com/svenski/pyterminit',
      author='Sergiusz Bleja',
      author_email='sergiusz@bleja.org',
      license='MIT',
      long_description=long_description,
      packages=['ipyterminit'],
      keywords=['ipython','ssh', 'vim'])


      
