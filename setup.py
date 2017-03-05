from setuptools import setup
from os import path

setup(
    name='hebrew-special-numbers',
    version='2.1.0',
    description='Data for creating Hebrew numerals, including exceptional numeric forms',
    url='https://github.com/chaimleib/hebrew-special-numbers',
    author='Chaim-Leib Halbert',
    author_email='chaim.leib.halbert@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='gematria hebrew numerals',
    extras_require={
        'test': ['pyyaml'],
    },
    data_files=[('styles', ['styles/*.yml'])],
    test_suite='test',
)
