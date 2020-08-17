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


import pandas as pd
import math
from tabulate import tabulate

MAX_PRINT_COLUMNS = 5
MAX_ROWS_TO_PRINT = 5


def parse_parquet_file(parquet_path, **kwargs):

    print(parquet_path)
    print(kwargs)

    # print(kwargs["header"])

    # dataframe = pd.read_parquet(parquet_path)
    # dataframe_to_print = dataframe.head(MAX_ROWS_TO_PRINT)

    # print_dataframe_content(dataframe_to_print)


def print_dataframe_content(dataframe):
    dataframe_len = len(dataframe.columns)
    total_block_size = math.ceil((dataframe_len/MAX_PRINT_COLUMNS))
    START_COLUMN_INDEX = 1
    INDEX_OFFSET = 1

    block_count_elements = 1
    dataframe_buffer = None
    dataframe_index_columns = []
    for x in range(START_COLUMN_INDEX, total_block_size):

        if total_block_size-INDEX_OFFSET == x:
            dataframe_index_columns = list(
                range(block_count_elements, dataframe_len))
            dataframe_buffer = dataframe.iloc[:, dataframe_index_columns].copy(
            )
            print(tabulate(dataframe_buffer, headers='keys', tablefmt='psql'))

        elif not x == total_block_size:
            block_final_size = block_count_elements+MAX_PRINT_COLUMNS
            dataframe_index_columns = list(
                range(block_count_elements, block_final_size))
            dataframe_buffer = dataframe.iloc[:, dataframe_index_columns].copy(
            )
            print(tabulate(dataframe_buffer, headers='keys', tablefmt='psql'))

            block_count_elements = block_count_elements+MAX_PRINT_COLUMNS
