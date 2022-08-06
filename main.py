from lib.calculator_express import CalculatorExpress
from lib.sub_lib.char_expression import CharComponent


def on_running_program():
    progression = input('Insert your progression: ').split(',')
    term = int(input('Insert term of progression: '))
    
    CalculatorExpress.progressionGeometryCrescent(progression, term)
    


if __name__ == '__main__':
    on_running_program()
