from typing import Dict
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(NumpyHandler())

    response = calculator_3.calculate(mock_request)
    print()
    print(response)