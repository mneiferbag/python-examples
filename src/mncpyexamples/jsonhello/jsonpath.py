"""Basic JSONPath usage examples.

Copyright (c) 2025 Markus Neifer
Licensed under the MIT License.
See file LICENSE in project root directory.

See https://github.com/h2non/jsonpath-ng
"""
import jsonpath_ng as jp

def parse_no_space():
    """Parse JSONPath without spaces."""
    jsonpath_expr = jp.parse('foo[*].baz')

    return [match.value for match in jsonpath_expr.find({'foo': [{'baz': 1}, {'baz': 2}]})]

def parse_with_space():
    """Parse JSONPath with spaces."""
    jsonpath_expr = jp.parse('"foo bar"[*].baz')

    return [match.value for match in jsonpath_expr.find({'foo bar': [{'baz': 1}, {'baz': 2}]})]

if __name__ == '__main__':
    print('parse_no_space:', parse_no_space())
    print('parse_with_space:', parse_with_space())
