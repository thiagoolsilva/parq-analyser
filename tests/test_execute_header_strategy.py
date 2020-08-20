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
from source.parquet_core import execute_header_strategy


class TestParquetHeaderFunc(unittest.TestCase):

    def test_when_args_equals_to_one_is_expected_to_return_one_element(self):
        dataframe = create_dataframe(3)
        filtered_element = execute_header_strategy(dataframe, 1)

        self.assertEqual(1, len(filtered_element.index))

    def test_when_args_equals_to_zero_is_expected_to_return_no_element(self):
        dataframe = create_dataframe(3)
        filtered_element = execute_header_strategy(dataframe, 0)

        self.assertEqual(0, len(filtered_element.index))

    def test_when_args_equals_to_two_is_expected_to_return_two_element(self):
        dataframe = create_dataframe(3)
        filtered_element = execute_header_strategy(dataframe, 2)

        self.assertEqual(2, len(filtered_element.index))

    def test_when_args_equals_to_None_is_expected_to_return_one_element(self):
        dataframe = create_dataframe(6)
        filtered_element = execute_header_strategy(dataframe, None)

        self.assertEqual(5, len(filtered_element.index))

    def test_when_args_equals_to_five_is_expected_to_return_zero_elements(self):
        dataframe = create_dataframe(5)
        filtered_element = execute_header_strategy(dataframe, 5)

        self.assertEqual(5, len(filtered_element.index))

    def test_when_args_is_bigger_then_dataframe_len_is_expected_to_return_all_elements(self):
        dataframe = create_dataframe(5)
        filtered_element = execute_header_strategy(dataframe, 10)

        self.assertEqual(5, len(filtered_element.index))

    def test_when_args_equals_one_is_expected_to_return_the_first_elements(self):
        dataframe = create_dataframe(5)
        filtered_element = execute_header_strategy(dataframe, 1)

        self.assertEqual(1, len(filtered_element.index))
        self.assertEqual(0, filtered_element.index)


if __name__ == '__main__':
    unittest.main()
