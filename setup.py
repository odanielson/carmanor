from distutils.core import setup

setup(
    name='Carmanor',
    version='0.1.1',
    author='Olov Danielson',
    author_email='olov.danielson@gmail.com',
    packages=['carmanor'],
    package_dir={'carmanor': 'src'},
    scripts=['bin/harvester'],
    url='https://github.com/odanielson/carmanor/',
    license='LICENSE',
    description='Simple log harvesting tool.',
    long_description=open('README.md').read()
)
