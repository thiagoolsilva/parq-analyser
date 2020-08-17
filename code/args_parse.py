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

import os
import argparse


def config_args_parse(version):
    """
    Process args parse.

    Current supported arguments
     -P --path   the path of parquet file
     -H --head   The numbers of the first rows to be returned. The default is 5 and the maximum accepted is 39

    Returns:
        [ArgumentParser]: Argument parse instance
    """

    # check if was provided the program version
    if not version:
        raise ValueError('It was not provided a valid version')

    # configure the ArgumentParse
    parser = argparse.ArgumentParser(
        description='Process parquet file data', epilog='Enjoy the program!')
    parser.version = version

    # configure supported arguments
    parser.add_argument('-P',
                        metavar='--path',
                        type=str,
                        action='store',
                        help='the path of parquet file')
    parser.add_argument('-H',
                        metavar='--head',
                        type=int,
                        required=False,
                        choices=range(1, 40),
                        action='store',
                        help='The numbers of the first rows to be returned. The default is 5 and the maximum accepted is 39')
    parser.add_argument('-v',
                        action='version',
                        help='Shows the app version')

    # parse received arguments
    args = parser.parse_args()

    parquet_file_path = args.P
    # check if the provided path exists
    if not os.path.exists(parquet_file_path):
        raise FileNotFoundError('the provided file ' +
                                parquet_file_path + ' does not exists')

    return args
