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
import pandas as pd
from tests.dataframe_factory import create_dataframe
from source.parquet_core import execute_drop_strategy


class TestParquetCore(unittest.TestCase):

    def test_when_args_equals_to_one_is_expected_to_remove_one_element(self):
        dataframe = create_dataframe(3)
        execute_drop_strategy(dataframe, 1)

        self.assertEqual(2, len(dataframe.index))

    def test_when_args_equals_to_zero_is_expected_to_do_not_remove_element(self):
        dataframe = create_dataframe(3)
        execute_drop_strategy(dataframe, 0)

        self.assertEqual(3, len(dataframe.index))

    def test_when_args_equals_to_two_is_expected_to_remove_two_element(self):
        dataframe = create_dataframe(3)
        execute_drop_strategy(dataframe, 2)

        self.assertEqual(1, len(dataframe.index))

    def test_when_args_equals_to_None_is_expected_to_remove_five_element(self):
        dataframe = create_dataframe(6)
        execute_drop_strategy(dataframe, None)

        self.assertEqual(1, len(dataframe.index))

    def test_when_args_equals_to_five_is_expected_to_remove_all_elements(self):
        dataframe = create_dataframe(5)
        execute_drop_strategy(dataframe, 5)

        self.assertEqual(0, len(dataframe.index))

    def test_when_args_is_bigger_then_dataframe_len_is_expected_to_remove_all_elements(self):
        dataframe = create_dataframe(5)
        execute_drop_strategy(dataframe, 10)

        self.assertEqual(0, len(dataframe.index))

    def test_when_args_equals_one_len_is_expected_to_remove_first_element(self):
        dataframe = create_dataframe(3)
        execute_drop_strategy(dataframe, 1)

        first_row = dataframe.head(1)

        self.assertEqual(2, len(dataframe.index))
        self.assertEqual(1, first_row.index)


if __name__ == '__main__':
    unittest.main()
