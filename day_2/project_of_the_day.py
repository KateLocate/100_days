# https://replit.com/@appbrewery/tip-calculator-end
from typing import Callable


class TipCalculator:
    GREETING = 'Welcome to the tip calculator!'
    ASK_TOTAL_BILL = 'What was the total bill?'
    TIP_PERCENTS = (10, 12, 15)
    ASK_TIP_PERCENT = 'How much tip would you like to give? {}, {}, or {}?'.format(*TIP_PERCENTS)
    NUMBER_OF_PEOPLE = (1, float('inf'))
    ASK_NUMBER_OF_PEOPLE = 'How many people to split the bill?'
    TELL_THE_RESULT = 'Each person should pay: ${:.2f}'
    BILL_VALUE_ERROR_MESSAGE = 'Please, enter positive number.'
    PEOPLE_VALUE_ERROR_MESSAGE = 'Please, use positive integers greater than 0, e.g. 1, 2, 5.'
    TIP_ERROR_MESSAGE = 'Please, choose the tip amount from the given options.'

    def get_number(self, data_type: type, input_message: str, error_message: str, check: Callable = None):
        try:
            result = data_type(input(input_message))
        except ValueError:
            print(error_message)
            result = self.get_number(data_type, input_message, error_message)
        if check:
            if not check(result):
                print(error_message)
                result = self.get_number(data_type, input_message, error_message, check=check)
        return result

    def run_calculator(self):
        print(self.GREETING)

        bill = self.get_number(float, self.ASK_TOTAL_BILL, self.BILL_VALUE_ERROR_MESSAGE, check=lambda x: x >= 0)
        tip_percent = self.get_number(
            int, self.ASK_TIP_PERCENT, self.TIP_ERROR_MESSAGE, check=lambda x: x in self.TIP_PERCENTS
        )
        num_of_people = self.get_number(
            int, self.ASK_NUMBER_OF_PEOPLE, self.PEOPLE_VALUE_ERROR_MESSAGE,
            check=lambda x: self.NUMBER_OF_PEOPLE[0] < x < self.NUMBER_OF_PEOPLE[1]
        )

        bill_with_tip = bill + tip_percent * bill / 100
        part_of_bill_divided = bill_with_tip / num_of_people

        print(self.TELL_THE_RESULT.format(part_of_bill_divided))


if __name__ == '__main__':
    calculator = TipCalculator()
    calculator.run_calculator()
