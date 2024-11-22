import pytest
from calculator import Calculator

calculator=Calculator()


@pytest.mark.parametrize("num1, num2, result",[(4,5,9),(-6,-10,-16),(-6,6,0),(5.61, 4.29, 9.9),(10,0,10)])
def test_sum_nums(num1,num2,result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result
    

@pytest.mark.parametrize("nums, result",[([], 0), ([1,2,3,4,5,6,7,8,9,5], 5)])
def test_avg_list(nums, result):
    calculator=Calculator()
    res = calculator.avg(nums)
    assert res == result


def test_div_positive():
    calculator=Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_zero():
    calculator=Calculator()
    import pytest
    with pytest.raises(ArithmeticError):
        res = calculator.div(10, 0)