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
from source.parquet_core import validate_required_fields


class TestParquetValidateFunc(unittest.TestCase):

    def test_when_dataframe_is_None_is_expected_raise_exception(self):
        dataframe = None

        self.assertRaises(
            ValueError, lambda: validate_required_fields(dataframe))

    def test_when_dataframe_is_not_empty_is_expected_do_not_raise_exception(self):
        dataframe = create_dataframe(1)

        validate_required_fields(dataframe)


if __name__ == '__main__':
    unittest.main()
