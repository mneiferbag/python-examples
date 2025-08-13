"""Test the jsonpath module.

Copyright (c) 2025 Markus Neifer
Licensed under the MIT License.
See file LICENSE in project root directory.
"""
from mncpyexamples.jsonhello import jsonpath

def test_parse_no_space():
    """Test JSONPath parsing without spaces."""
    result = jsonpath.parse_no_space()
    assert result == [1, 2]

def test_parse_with_space():
    """Test JSONPath parsing with spaces."""
    result = jsonpath.parse_with_space()
    assert result == [1, 2]
