"""Test the helloasync module.

Copyright (c) 2025 Markus Neifer
Licensed under the MIT License.
See file LICENSE in project root directory.
"""
from mncpyexamples.asynchello import helloasync

def test_helloasync(capsys):
    """Test the run_main() function."""
    helloasync.run_main()
    captured = capsys.readouterr()
    assert captured.out == "Hello ...\n... World!\n"
