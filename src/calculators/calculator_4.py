from flask import request as FlaskRequests
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequests) -> Dict: # type: ignore
        body = request.json
        imput_data = self.__validate_body(body)
        average = self.__process_data(imput_data)
        formated_response = self.__format_response(average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError('body does not contain numbers! - incorrect format! \n Examble format: {"numbers": [3.4, 4, 64.13]}')
        
        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        average = self.__driver_handler.average(input_data)
        return average
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": average,
                "success": True
        }
    }