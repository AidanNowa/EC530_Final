import pytest
import program1 as p1

expression = "(A & B) | (~C & D) | (A & ~B) | (C & ~D)"
symbols_str = "A B C D"
minterms = p1.boolean_expression_to_minterms(expression, symbols_str)
maxterms = p1.boolean_expression_to_maxterms(expression, symbols_str)

binary_minterms = p1.convert_minterms_to_binary(minterms)
minterm_indices = p1.minterms_to_indices(binary_minterms)
binary_maxterms = p1.convert_minterms_to_binary(maxterms)
maxterm_indices = p1.minterms_to_indices(binary_maxterms)
sop_expression = p1.minterms_to_canonical_sop(minterms)
pos_expression = p1.minterms_to_canonical_sop(maxterms)
minimized_sop = p1.simplify(sop_expression, symbols_str)
minimized_pos = p1.simplify(pos_expression,symbols_str)

def test_boolean_expression_to_minterms():
    assert p1.boolean_expression_to_minterms("A & B", "A B") == ["A & B"], "Test failed for AND operation"

def test_boolean_expression_to_maxterms():
    assert p1.boolean_expression_to_maxterms(expression, symbols_str) == ['~A & ~B & ~C & ~D', '~A & ~B & C & D', '~A & B & ~C & ~D', '~A & B & C & D'], "Test Success"

def test_canonical_sop():
    assert str(minterm_indices) == "[1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]", "Success"

def test_canonical_pos():
    assert str(maxterm_indices) == "[0, 3, 4, 7]", "Success"

def test_min_sop():
    assert str(minimized_sop) == "A | (C & ~D) | (D & ~C)", "Success"

def test_min_pos():
    assert str(minimized_pos) == "~A & (C | ~D) & (D | ~C)", "Success"



