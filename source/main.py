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
from source.args_parse import config_args_parse
from source.dataframe_helper import load_dataframe
from source.parquet_core import parse_parquet_file
from source.version import __version__


def main():
    """
    Process parquet file data
    """

    try:
        # start args parse module
        args = config_args_parse(__version__)

        # check if verbose mode need to be activated
        should_activate_verbose_mode(args.verbose)

        logging.debug(vars(args))

        # load dataframe
        dataframe = load_dataframe(args.P)

        # call parquet core
        parse_parquet_file(
            dataframe, header=args.H, tail=args.T,
            total_dataframe_size=args.C, drop_rows=args.D,
            selected_columns=args.CS)

    except Exception as e:
        logging.error(str(e))


def should_activate_verbose_mode(verbose_mode):
    """
    Check if verbose mode must be activated

    Args:
        verbose_mode (Bool): True if need to activate verbose mode
    """

    if verbose_mode:
        logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    main()
