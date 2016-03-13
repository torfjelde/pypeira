from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import pypeira

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []

    for filename in filenames:
        try:
            import pypandoc
            description = pypandoc.convert(filename, 'rst')

            buf.append(description)
        except:
            with io.open(filename, encoding=encoding) as f:
                buf.append(f.read())

    return sep.join(buf)


long_description = read('README.md') # TODO: Add 'CHANGES.md'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_test(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='pypeira',
    version=pypeira.__version__,
    url='http://github.com/WielderOfMjoelnir/pypeira/',
    license='Apache Software License',
    author='Tor Erlend Fjelde',
    tests_require=['pytest'],
    install_requires=['numpy',
                      'matplotlib',
                      'fitsio',
                      'pandas'
                    ],
    cmdclass={'test': PyTest},
    author_email='tor.github@gmail.com',
    description='',
    long_description=long_description,
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    include_package_data=True,
    platforms='any',
    test_suite='pypeira.test.test_pypeira',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
        ],
    extras_require={
        'testing': ['pytest'],
    }
)