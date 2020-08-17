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

import argparse
import args_parse
import parquet_core


def main():
    """
    Process parquet file data
    """

    args = args_parse.config_args_parse('01.00.00')
    print(vars(args))

    parquet_core.parse_parquet_file(args.P)


main()
