# """
# test_exercise15_7
# """
from exercise15_7 import Die
from random import randint
import pytest

# # 测试方法一：不使用夹具
def test_roll_within_range_6_sides():
    die = Die()
    result = die.roll()
    assert 1 <= result <= die.num_sides

# # 测试方法二：使用夹具
@pytest.fixture
def die():
    '''创建一个骰子实例的夹具'''
    return Die()

def test_roll(die):
    '''测试掷骰子的结果是否在1到骰子面数之间'''
    result = die.roll()
    assert 1 <= result <= die.num_sides











