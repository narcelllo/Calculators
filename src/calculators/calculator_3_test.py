from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def variance(self, numbers: List[float]) -> float:
        return 1000000

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(NumpyHandler())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)
        assert str(excinfo.value) == 'failed: variance < multiplication'

def test_calculate_integrate_test():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(NumpyHandler())

    response = calculator_3.calculate(mock_request)
    assert response == {'data': {'Calculator': 3, 'value': 1568.16, 'success': True}}
    
def test_calculate_test():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)
    assert response == {'data': {'Calculator': 3, 'value': 1000000, 'success': True}}    
