from pythonisms import __version__
import pytest
from pythonisms.linked_list import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_import():
    assert LinkedList

def test_linked():
    linked = LinkedList([1,2,3,4,5])

    actual = str(linked)
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None'
    assert actual == expected

def test_len():
    linked = LinkedList([1,2,3,4,5])
    
    actual = len(linked)
    expected = 5
    assert actual == expected

def test_len_empty():
    linked = LinkedList()
    
    actual = len(linked)
    expected = 0
    assert actual == expected

def test_get_item():
    linked = LinkedList([1,2,3,4,5])
    
    actual = linked[0]
    expected = 1
    assert actual == expected

def test_get_item_end():
    linked = LinkedList([1,2,3,4,5])
    
    actual = linked[4]
    expected = 5
    assert actual == expected

def test_for_in():
    nums = []
    linked = LinkedList([1,2,3,4,5])
    for num in linked:
        nums.append(num)
    
    actual = nums
    expected = [1,2,3,4,5]
    assert actual == expected

def test_comprehension():

    linked = LinkedList([1,2,3,4,5])
    nums = [x for x in linked]
    
    actual = nums
    expected = [1,2,3,4,5]
    assert actual == expected

def test_list():

    linked = LinkedList([1,2,3,4,5])
    
    actual = list(linked)
    expected = [1,2,3,4,5]
    assert actual == expected

def test_range():

    num_range = range(1, 20 + 1)

    nums = LinkedList(num_range)

    actual = len(nums) 
    expected = 20
    assert actual == expected

def test_next():

    foods = LinkedList(["apple", "banana", "cucumber"])

    iterator = iter(foods)

    assert next(iterator) == "apple"
    assert next(iterator) == "banana"
    assert next(iterator) == "cucumber"


def test_stop_iteration():

    foods = LinkedList(["apple", "banana", "cucumber"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            next(iterator)

def test_eq():

    num_range = range(1, 20 + 1)

    nums = LinkedList(num_range)
    nums2 = LinkedList(num_range)

    assert nums == nums2

def test_set():

    nums = LinkedList([1,2,3,4,5])

    nums[0] = 0

    actual = nums[0]
    expected = 0
    assert actual == expected

def test_set_end():

    nums = LinkedList([1,2,3,4,5])

    nums[4] = 0

    actual = nums[4]
    expected = 0
    assert actual == expected