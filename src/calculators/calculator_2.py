from flask import request as FlaskRequests
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequests) -> Dict: # type: ignore
        body = request.json
        imput_data = self.__validate_body(body)
        calculated_number = self.__process_data(imput_data)
        formated_response = self.__format_response(calculated_number)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception('body does not contain numbers! - incorrect format! \n Examble format: {"numbers": [3.4, 4, 64.13]}')
        
        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.96 for num in input_data]
        result = self.__driver_handler.standarf_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
        }
    }