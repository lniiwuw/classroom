import pytest
from src.calculator import add, subtract, multiply, divide, is_even

class TestBasicOperations:
    """测试基础运算功能"""
    
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(10, -5) == 15
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(7, 0) == 0
    
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(9, 4) == 2.25
        
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)

class TestAdvancedFeatures:
    """测试进阶功能"""
    
    @pytest.mark.parametrize("num,expected", [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-5, False)
    ])
    def test_is_even(self, num, expected):
        assert is_even(num) == expected