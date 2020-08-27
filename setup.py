"""
Copyright (c) 2020  Thiago Lopes da Silva

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import find_packages, setup
import pathlib
import pkg_resources
import os
from source.version import __version__

# get requirement dependencies
with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

# get content of README.md file
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''


# execute setuptools script
setup(
    name='parq analyser',
    license='https://github.com/thiagoolsilva/parquet_reader/blob/master/LICENSE',
    author='Thiago Lopes da Silva <thiagoolsilva@gmail.com',
    version=__version__,
    description="It is a program that helps data sciences to analyze parquet files.",
    long_description=long_description,
    url="https://github.com/thiagoolsilva",
    packages=find_packages(include=['source'], exclude=['tests']),
    include_package_data=True,
    platforms='any',
    download_url='https://github.com/thiagoolsilva/parquet_reader',
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "parq-analyser = source.main:main",
        ]
    },
    python_requires='>=3.2',
    install_requires=install_requires
)
