
from challenge2 import dice_faces_calculator

def test_case_1():
    value = dice_faces_calculator([6, 6, 6])

    assert value == 18

def test_case_2():
    value = dice_faces_calculator([5, 5, 5])

    assert value == 15

def test_case_3():
    value = dice_faces_calculator([1, 2, 3])

    assert value == 3

def test_case_4():
    value = dice_faces_calculator([1, 3, 1])

    assert value == 2

def test_case_5():
    value = dice_faces_calculator([3, 5, 3])

    assert value == 6

def test_case_6():
    value = dice_faces_calculator([6, 5, 4])

    assert value == 6

def test_case_7():
    value = dice_faces_calculator([4, 5, 6])

    assert value == 6
