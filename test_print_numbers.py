import pytest
from print_numbers import print_numbers


def test_print_numbers_output(capsys):
    """Test that print_numbers prints 1 to 100."""
    print_numbers()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 100
    assert lines[0] == "1"
    assert lines[99] == "100"


def test_print_numbers_prints_all_integers():
    """Test that all numbers from 1 to 100 are printed."""
    from io import StringIO
    import sys
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    print_numbers()
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    lines = output.strip().split('\n')
    for i in range(1, 101):
        assert str(i) in lines
