import io
import os
import re
from setuptools import setup

with io.open("README.rst", mode='r', encoding='utf-8') as f:
    long_description = f.read()

with io.open("funcparse/__version__.py", mode='r',
             encoding='utf-8') as f:
    try:
        version = re.findall(
            r"^version = \"([^']+)\"\r?$", f.read(), re.M
        )[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")

setup(
    name='funcparse',
    version=version,
    author='SJQuant',
    license="MIT",
    author_email='seonujang92@gmail.com',
    description=(
        'Parse `funcname`, `args`, `kargs` from function-like string'
    ),
    url='https://github.com/sjquant/funcparse',
    long_description=long_description,
    packages=['funcparse'],
    keywords=['parse', 'parse function', 'string-to-function'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
