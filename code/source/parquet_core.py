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
import pandas as pd
import logging

MAX_ROWS_TO_PRINT = 5
DEFAULT_SELECTED_ROWS = 5


def parse_parquet_file(dataframe, **kwargs):
    """
    Parse the parquet content file

    Args:
        dataframe (pandas.Dataframe): dataframe
        kwargs (Any) Args
    """

    # check if the provided dataframe is valid
    validate_required_fields(dataframe)

    # log all arguments provided by client
    logging.debug(kwargs)

    # get all provided args
    arg_header_count = kwargs["header"]
    arg_tail_count = kwargs["tail"]
    args_total_dataframe_count = kwargs["total_dataframe_size"]
    args_drop_count = kwargs["drop_rows"]

    filtered_dataframe = None
    total_count_dataframe = None

    if args_drop_count:
        execute_drop_strategy(dataframe, args_drop_count)

    if args_total_dataframe_count:
        total_count_dataframe = execute_total_dataframe_count_strategy(dataframe)
    elif arg_tail_count:
        filtered_dataframe = execute_tail_strategy(dataframe, arg_tail_count)
    else:
        filtered_dataframe = execute_header_strategy(
            dataframe, arg_header_count)

    if filtered_dataframe is not None:
        print_dataframe_content(filtered_dataframe)
    else:
        print("Total Rows:", total_count_dataframe)


def execute_total_dataframe_count_strategy(dataframe):
    """
    Get total dataframe size

    Args:
        dataframe (pandas.Dataframe): Dataframe

    Returns:
        [int]: number of rows
    """

    logging.debug('>>>>>>>>> Using total count strategy <<<<<<<<<<<<')

    total_rows = len(dataframe.index)

    return total_rows


def execute_tail_strategy(dataframe, arg_tail_count):
    """
    Execute Tail strategy

    Args:
        dataframe (pandas.Dataframe): Dataframe
        arg_tail_count (int): number of rows to be returned

    Returns:
        [pandas.Dataframe]: Filtered Dataframe
    """

    logging.debug('>>>>>>>>> Using tail strategy <<<<<<<<<<<<')

    selected_tail_rows = DEFAULT_SELECTED_ROWS if arg_tail_count == None else arg_tail_count

    filtered_dataframe = dataframe.tail(selected_tail_rows)

    return filtered_dataframe


def execute_header_strategy(dataframe, arg_header_count):
    """
    Execute Header strategy

    Args:
        dataframe [pandas.Dataframe]: dataframe
        arg_header_count [int]: number of rows to be returned

    Returns:
        [pandas.Dataframe]: Filtered Dataframe
    """

    logging.debug('>>>>>>>>> Using header strategy <<<<<<<<<<<<')

    selected_header_rows = DEFAULT_SELECTED_ROWS if arg_header_count == None else arg_header_count

    filtered_dataframe = dataframe.head(selected_header_rows)

    return filtered_dataframe


def execute_drop_strategy(dataframe, arg_drop_count):
    """

    Drop the first elements of dataframe

    Args:
        dataframe (pandas.Dataframe): Dataframe
        arg_drop_count (int): rows to be dropped
    """

    logging.debug('>>>>>>>>> Using drop rows strategy <<<<<<<<<<<<')

    selected_drop_rows = DEFAULT_SELECTED_ROWS if arg_drop_count == None else arg_drop_count

    if selected_drop_rows == 1:
        dataframe = dataframe.drop(dataframe.index[0], inplace=True)
    else:
        dataframe.drop(dataframe.index[0:selected_drop_rows], inplace=True)


def validate_required_fields(dataframe):
    """
    Check if was provided a valid Dataframe

    Args:
        dataframe (pandas.Dataframe): Dataframe instance

    Raises:
        ValueError: If the Dataframe is not valid
    """

    if dataframe is None:
        raise ValueError("It was not provided a valid Dataframe.")


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
