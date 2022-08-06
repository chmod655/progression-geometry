import math
from rich import print
from lib.sub_lib.char_expression import CharComponent as char

class CalculatorExpress:

    def __init__(self) -> None:
        pass

    def progressionGeometryCrescent(pg, term):
        progressionList = [int(x) for x in pg]
        
        termToBeFound = term

        def getQuocient(termIndexSecond, termIndexFirst):
            return termIndexSecond // termIndexFirst

        def returnExpressionGeometryCres(termFirstIndex, quocient, term):
            quocient_calc = quocient**(term - 1)
            expression = termFirstIndex * quocient_calc

            return expression, quocient_calc
        
        quocient = getQuocient(progressionList[1], progressionList[0])
        expression, quocient_calc = returnExpressionGeometryCres(progressionList[0], quocient, termToBeFound)

        print(f'''Result of this PG: [{progressionList}] to find this term: [{termToBeFound}]

    A{char.subscript(f'{termToBeFound}')} = {progressionList[0]}.({quocient}{char.superscript(f'{termToBeFound}-1')})
    A{char.subscript(f'{termToBeFound}')} = {progressionList[0]}.{quocient_calc}
    A{char.subscript(f'{termToBeFound}')} = {expression}''')

    def progressionGeometryDecrescent():
        pass

    def progressionGeometryOscillating():
        pass

    def progressionGeometryConstant():
        pass
