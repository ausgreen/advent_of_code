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