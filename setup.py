import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pymeg',
    version='0.0.12',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=['pymeg'],
    description='Python mathematical expression generator',
    url='https://github.com/yjg30737/pymeg.git',
    long_description_content_type='text/markdown',
    long_description=long_description
)