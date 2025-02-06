from lib.high_value import *

"""
Testing making an instance of the class
"""
def test_make_an_instance():
    high_value_1 = HighValue(4, 3)
    assert isinstance(high_value_1, HighValue)

"""
Test value_first and value_second properties assigned correctly
"""
def test_value_first_and_value_second_properties():
    high_value_1 = HighValue(4, 3)
    assert high_value_1.value_first == 4
    assert high_value_1.value_second == 3

"""
Test get_highest recognises highest value when value_first is higher
"""
def test_get_highest_when_first_is_higher():
    high_value_1 = HighValue(6,5)
    expected = "First value is higher"
    actual = high_value_1.get_highest()
    assert actual == expected

"""
Test get_highest recognises highest value when value_second is higher
"""
def test_get_highest_when_second_is_higher():
    high_value_1 = HighValue(5,6)
    expected = "Second value is higher"
    actual = high_value_1.get_highest()
    assert actual == expected

"""
Test get_highest when both values equal
"""
def test_get_highest_when_both_values_equal():
    high_value_1 = HighValue(6,6)
    expected = "Values are equal"
    actual = high_value_1.get_highest()
    assert actual == expected

"""
Test add() increments self.value_first correctly
"""
def test_add_method_increments_value_first_correctly():
    high_value_1 = HighValue(5, 10)
    high_value_1.add(5, "first")
    expected_first_value = 10
    expected_second_value = 10
    actual_first_value = high_value_1.value_first
    actual_second_value = high_value_1.value_second
    assert actual_first_value == expected_first_value
    assert actual_second_value == expected_second_value

"""
Test add() increments self.value_second correctly
"""
def test_add_method_increments_value_second_correctly():
    high_value_1 = HighValue(5, 10)
    high_value_1.add(5, "second")
    expected_first_value = 5
    expected_second_value = 15
    actual_first_value = high_value_1.value_first
    actual_second_value = high_value_1.value_second
    assert actual_first_value == expected_first_value
    assert actual_second_value == expected_second_value