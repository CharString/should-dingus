from setuptools import setup
import should_dingus

setup(
    name='should-dingus',
    version=should_dingus.__version__,
    author='Chris Wesseling',
    author_email='chris.wesseling@cwi.nl',
    url='https://github.com/CharString/should-dingus',
    description='Dingus call matcher for should-dsl',
    long_description=open('README.rst').read(),
    classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        ],
    license='BSD',
    keywords='dingus should dsl testing test mocking mock double stub fake record assert bdd python expectation',
    py_modules=['should_dingus'],
    install_requires=['dingus',
                      'should-dsl'
                     ]
    )
