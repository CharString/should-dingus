from setuptools import setup
from os import path


long_desc = open(path.join(path.dirname(__file__), 'README.rst')).read()

install_req = ['dingus', 'should-dsl']
setup_req = install_req + ['nose']

setup(
    name='should-dingus',
    version='0.3',
    author='Chris Wesseling',
    author_email='chris.wesseling@cwi.nl',
    url='https://github.com/CharString/should-dingus',
    description='Dingus call matcher for should-dsl',
    long_description=long_desc,
    classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        ],
    license='BSD',
    keywords=('dingus should dsl testing test mocking '
        'mock double stub fake record assert bdd python expectation'),
    py_modules=['should_dingus'],
    tests_requires=setup_req,
    setup_requires=setup_req,
    install_requires=install_req,
    )
