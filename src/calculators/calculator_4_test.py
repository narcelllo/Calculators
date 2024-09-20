from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def average(self, numbers: List[float]) -> float:
        return 1
    
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    calculator_4 = Calculator4(NumpyHandler())
    formated_response = calculator_4.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == {
                                    "data": {
                                        "Calculator": 4,
                                        "success": True,
                                        "value": 2.686666666666667
                                    }
                                }
    
def test_calculate_with_error():
    mock_request = MockRequest({"number": []})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
        assert str(excinfo.value) == 'body does not contain numbers! - incorrect format! \n Examble format: {"numbers": [3.4, 4, 64.13]}'

def test_calculate_test():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)
    assert response == {
                            "data": {
                                "Calculator": 4,
                                "success": True,
                                "value": 1.0
                            }
                        }