from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body= {"number": 3})
    calculator1 = Calculator1()

    response = calculator1.calculate(mock_request)
    
    # Teste response format
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertiveness response
    assert response["data"]["result"] == 15.7085625
    assert response["data"]["Calculator"] == 1
 
def test_calculate_with_body_error():
    mock_request = MockRequest(body= {"something": 3})
    calculator1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator1.calculate(mock_request)

    assert str(excinfo.value) == 'body does not contain numbers! - incorrect format! \n Examble format: {"number": 3}'