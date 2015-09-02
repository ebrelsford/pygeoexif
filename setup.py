import os
from setuptools import setup


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='ebrelsford@gmail.com',
    name='pygeoexif',
    classifiers=CLASSIFIERS,
    description="Simply get latitude and longitude from an image's EXIF data",
    license='MIT License',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=['pygeoexif'],
    url='http://github.com/ebrelsford/pygeoexif',
    version='0.0.1',
    zip_safe=False,
)
