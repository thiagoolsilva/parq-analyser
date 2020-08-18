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


from tabulate import tabulate
from pprint import pprint
import pandas as pd
import math
import logging

MAX_ROWS_TO_PRINT = 5


def parse_parquet_file(parquet_path, **kwargs):
    """
    Parse the parquet content file

    Args:
        parquet_path (string): parquet path file
    """

    logging.debug(kwargs)

    # get all provided args
    arg_header_count = kwargs["header"]
    arg_tail_count = kwargs["tail"]
    args_total_dataframe_count = kwargs["total_dataframe_size"]

    # load parquet file
    dataframe = pd.read_parquet(parquet_path)

    if args_total_dataframe_count:
        logging.debug('>>>>>>>>> Using total count strategy <<<<<<<<<<<<')

        total_rows = len(dataframe.index)

        print("Total Rows:", total_rows)

    elif arg_tail_count:
        logging.debug('>>>>>>>>> Using tail strategy <<<<<<<<<<<<')

        selected_tail_rows = MAX_ROWS_TO_PRINT if arg_tail_count == None else arg_tail_count

        filtered_dataframe = get_dataframe_tail(dataframe, selected_tail_rows)

        print_dataframe_content(filtered_dataframe)
    else:
        logging.debug('>>>>>>>>> Using header strategy <<<<<<<<<<<<')

        selected_header_rows = MAX_ROWS_TO_PRINT if arg_header_count == None else arg_header_count

        filtered_dataframe = get_dataframe_header(
            dataframe, selected_header_rows)

        print_dataframe_content(filtered_dataframe)


def get_dataframe_tail(dataframe, selected_rows):
    """
    Get the tail rows of dataframe

    Args:
        dataframe (pandas.Dataframe): Dataframe
        selected_rows (int): number of rows

    Returns:
        pandas.Dataframe: Filtered dataframe
    """
    return dataframe.tail(selected_rows)


def get_dataframe_header(dataframe, selected_rows):
    """
    Get the first rows from provided dataframe

    Args:
        dataframe [pandas.Dataframe]: dataframe
        selected_rows [int]: number of rows to be returned

    Returns:
        [pandas.Dataframe]: filtered dataframe
    """

    return dataframe.head(selected_rows)


def print_dataframe_content(dataframe):
    """
    Print out dataframe data

    Args:
        dataframe (pandas.Dataframe): Dataframe
    """

    dataframe_len = len(dataframe.columns)
    dataframe_columns_index = list(range(0, dataframe_len))
    dataframe_column_index_len = len(dataframe_columns_index)

    if dataframe.empty:
        print('Empty dataframe.')
    else:
        should_continue_process = True
        current_process_batch_size = 0

        while should_continue_process:
            slide_object = slice(current_process_batch_size,
                                 current_process_batch_size+MAX_ROWS_TO_PRINT)
            dataframe_index_columns = dataframe_columns_index[slide_object]

            current_process_batch_size = current_process_batch_size+MAX_ROWS_TO_PRINT

            dataframe_buffer = dataframe.iloc[:,
                                              dataframe_index_columns].copy()
            print(tabulate(dataframe_buffer, headers='keys', tablefmt='psql'))

            if current_process_batch_size >= dataframe_column_index_len:
                should_continue_process = False
