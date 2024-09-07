from typing import Dict
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calulate():
    mock_request = MockRequest(body= {"number": 3})
    calculator1 = Calculator1()

    response = calculator1.calculate(mock_request)
    print()
    print(response)

    # Teste response format
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertiveness response
    assert response["data"]["result"] == 15.7085625
    assert response["data"]["Calculator"] == 2
