import pytest
import program1 as p1

def test_boolean_expression_to_minterms():
    assert p1.boolean_expression_to_minterms("A & B", "A B") == ["A & B"], "Test failed for AND operation"