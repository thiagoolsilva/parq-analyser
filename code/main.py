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

import logging
import argparse
import args_parse
import parquet_core


def main():
    """
    Process parquet file data
    """

    args = args_parse.config_args_parse('01.00.00')

    # check if verbose mode need to be activated
    should_activate_verbose_mode(args.verbose)

    logging.debug(vars(args))

    parquet_core.parse_parquet_file(args.P, header=args.H, tail=args.T, total_dataframe_size=args.C)

def should_activate_verbose_mode(verbose_mode):
    """
    Check if verbose mode must be activated

    Args:
        verbose_mode (Bool): True if need to activate verbose mode
    """

    if verbose_mode:
        logging.basicConfig(level=logging.DEBUG)

main()
