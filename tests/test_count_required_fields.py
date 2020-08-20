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
from source.parquet_core import execute_total_dataframe_count_strategy


class TestParquetValidateFunc(unittest.TestCase):

    def test_when_dataframe_has_len_equals_to_five_is_expected_to_return_five(self):
        dataframe = create_dataframe(5)
        dataframe_len = execute_total_dataframe_count_strategy(dataframe)

        self.assertEqual(5, dataframe_len)

    def test_when_dataframe_has_len_equals_to_zero_is_expected_to_return_zero(self):
        dataframe = create_dataframe(0)
        dataframe_len = execute_total_dataframe_count_strategy(dataframe)

        self.assertEqual(0, dataframe_len)


if __name__ == '__main__':
    unittest.main()
