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

import unittest
from tests.dataframe_factory import create_dataframe
from source.parquet_core import execute_select_dataframe_columns


class TestParquetTailFunc(unittest.TestCase):

    def test_when_provided_valid_columns_is_expected_to_return_them(self):

        valid_dataframe = create_dataframe(2)

        selected_columns = ["Number"]

        result_dataframe = execute_select_dataframe_columns(
            valid_dataframe, selected_columns)

        self.assertEqual(is_same_array(
            result_dataframe.columns, selected_columns), True)

    def test_when_provided_empty_columns_is_expected_to_return_all_columns(self):

        valid_dataframe = create_dataframe(2)

        invalid_selected_columns = []

        dataframe_result = execute_select_dataframe_columns(
            valid_dataframe, invalid_selected_columns)

        self.assertEqual(len(dataframe_result), len(valid_dataframe))

    def test_when_provided_invalid_columns_is_expected_to_raise_exception(self):

        valid_dataframe = create_dataframe(2)

        invalid_selected_columns = ["Invalid"]

        self.assertRaises(
            ValueError, lambda: execute_select_dataframe_columns(valid_dataframe, invalid_selected_columns))


def is_same_array(first, second):
    """

    Check if two arrays of strings are equals

    Args:
        first (array[str]): Array of strings
        second (array[str]): Array of string

    Returns:
        int: True if both are equals
    """

    diff_selected_columns = list(set(first) - set(second))

    return len(diff_selected_columns) == 0


if __name__ == '__main__':
    unittest.main()
