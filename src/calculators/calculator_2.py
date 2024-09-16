from flask import request as FlaskRequests
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
    def calculate(self, request: FlaskRequests) -> Dict: # type: ignore
        body = request.json
        imput_data = self.__validate_body(body)
        calculated_number = self.__process_data(imput_data)
        formated_response = self.__format_response(calculated_number)
        return formated_response

    def __validate_body(self,body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception('body does not contain numbers! - incorrect format! \n Examble format: {"number": 3}')
        
        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        numpy_hendler = NumpyHandler()
        first_process_result = [(num * 11) ** 0.96 for num in input_data]
        result = numpy_hendler.standarf_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
        }
    }