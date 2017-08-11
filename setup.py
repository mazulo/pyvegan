import sys
from setuptools import setup, find_packages


def read(fname):
    """ Return file content. """
    with open(fname) as f:
        content = f.read()

    return content


description = 'PyVegan is a simple Python CLI to browse vegan recipes'
try:
    long_description = read('README.rst')
except IOError:
    long_description = description


author_name = 'Patrick Mazulo'
author_email = 'pmazulo@gmail.com'
dependencies = [
    'curses-menu==0.5.0',
    'requests==2.18.1',
    'tqdm==4.14.0',
]

if sys.version_info.major == 2:
    dependencies.append('futures==3.0.5')

setup(
    name='PyVegan',
    version='0.1',
    description=description,
    long_description=long_description,
    url='https://github.com/mazulo/pyvegan',
    author=author_name,
    author_email=author_email,
    maintainer=author_name,
    maintainer_email=author_email,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Shells',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='pyvegan cli shell vegan',
    download_url='https://github.com/mazulo/pyvegan/archive/master.zip',
    packages=find_packages(exclude=['tests*']),
    install_requires=dependencies,
    entry_points={'console_scripts': ['pyvegan = pyvegan:main']},
    platforms='windows linux',
)
