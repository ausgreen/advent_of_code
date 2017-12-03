'''
Testing cases for aoc

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second
    digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the
last digit, 9.

'''
import pytest

def test_day_1():
    import aoc_01_captcha

    assert aoc_01_captcha.day_01(1122) == 3
    assert aoc_01_captcha.day_01(1111) == 4
    assert aoc_01_captcha.day_01(1234) == 0
    assert aoc_01_captcha.day_01(91212129) == 9

def test_day_2():
    import day_02

    assert day_02.day_02('''5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8''') == 18