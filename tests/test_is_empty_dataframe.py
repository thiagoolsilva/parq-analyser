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
from source.parquet_core import is_empty_dataframe


class TestParquetTailFunc(unittest.TestCase):

    def test_when_dataframe_is_empty_is_expected_to_return_true(self):

        empty_dataframe = create_dataframe(0)

        result_dataframe = is_empty_dataframe(empty_dataframe)

        self.assertEqual(result_dataframe, True)

    def test_when_dataframe_is_no_empty_is_expected_to_return_false(self):

        no_empty_dataframe = create_dataframe(1)

        result_dataframe = is_empty_dataframe(no_empty_dataframe)

        self.assertEqual(result_dataframe, False)


if __name__ == '__main__':
    unittest.main()
