from flask import request as FlaskRequest
from typing import Dict

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splites_number = input_data / 3

        first_process_result = self.__first_process(splites_number)
        second_process_result = self.__second_process(splites_number)
        calc_result = first_process_result + second_process_result + splites_number
        response = self.__format_response(calc_result)
        
        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception('body does not contain numbers! - incorrect format! \n Examble format: {"number": 3}')
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": calc_result
        }}
   