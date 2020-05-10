#-*-coding:utf-8-*-
import pytest
from apis.calc import Calc

class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expected", [
        (5, 5, 10),
        (-1, 0, -1),
        (0.5, 0.1, 0.6),
        (123456, 9455, 222222),
        ("a", 1, 'can only concatenate str (not "int") to str'),
        ([1], 1, 'can only concatenate list (not "int") to list'),
        (None, 1, "unsupported operand type(s) for +: 'NoneType' and 'int'")
    ])
    def test_add(self, a, b, expected):
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.add(a, b)
            assert result == expected
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expected", [
        (10, 5, 2),
        (7, 3, 7/3),
        (-1, 1, -1),
        (2, 0.1, 20.0),
        (0, 1, 0),
        (0, 0, "division by zero")
    ])

    def test_div(self, a, b, expected):
        # 除数为0
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a, b)
        # a,b 为整数或浮点数
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.div(a, b)
            assert result == expected
        # a,b 为其他数据类型
        else:
            with pytest.raises(TypeError):
                self.calc.div(a, b)


if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])
