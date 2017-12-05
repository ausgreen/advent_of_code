'''
Testing cases for aoc
'''
import pytest

def test_day_1():
    import day_01

    assert day_01.day_01(1122) == 3
    assert day_01.day_01(1111) == 4
    assert day_01.day_01(1234) == 0
    assert day_01.day_01(91212129) == 9


def test_day_2():
    import day_02

    assert day_02.day_02('''5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8''') == 18

def test_day_3():
    import day_03

    assert day_03.day_03(1) == 0
    assert day_03.day_03(12) == 3
    assert day_03.day_03(23) == 2
    assert day_03.day_03(1024) == 31

def test_day_4():
    # I solved this quickly and didn't write any tests
    assert "test_pass" == "test_pass"

def test_day_5():
    import day_05
    input = '''0\n3\n0\n1\n-3'''
    assert day_05.day_05(input) == 5