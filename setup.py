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

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


setup(
    name='parse parquet',
    license='https://github.com/thiagoolsilva/parquet_reader/blob/master/LICENSE',
    author='Thiago Lopes da Silva <thiagoolsilva@gmail.com',
    version='1.0.0',
    packages=find_packages(include=['source'], exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "parse_parquet = source.main:main",
        ]
    },
    setup_requires=['flake8'],
    python_requires='>=3.2',
    install_requires=install_requires
)
