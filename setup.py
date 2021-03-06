import os
import glob
import setuptools

PKG_NAME = 'start_core'

path = os.path.join(os.path.dirname(__file__), 'src', PKG_NAME, 'version.py')
with open(path, 'r') as f:
    exec(f.read())

setuptools.setup(
    name=PKG_NAME,
    version=__version__,
    description='Provides common data structures and helper methods for START',
    long_description='TBA',
    author='Chris Timperley',
    author_email='christimperley@gmail.com',
    url='https://github.com/ChrisTimperley/start-test-harness',
    # python_requires='>=3.5',
    install_requires=[
        'configparser',
        'attrs',
        # 'dronekit',
        # 'pymavlink>=2.2.10',
        'typing'
    ],
    include_package_data=True,
    packages=['start_core'],
    package_dir={'': 'src'},
    package_data={
        '': ['scenario.config.DEFAULT']
    },
    py_modules=[
        splitext(basename(path))[0] for path in glob.glob('start_core/*.py')
    ]
)
