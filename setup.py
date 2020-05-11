from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = None

setup(
    name='guillotina_scootermpi',
    version="1.0.0",
    description='A Master Patient Index ',
    long_description=README,
    install_requires=[
        'guillotina'
    ],
    author='Scooter Master Patient Index',
    author_email='david.bain@alteroo.com',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
