class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio = 1):
        if not isinstance(ratio, int) and not isinstance(ratio, float):
            raise ExamException("The ratio inserted is not correct")
        if ratio <= 0:
            raise ExamException("The ratio cannot be 0")
            
        self.ratio = ratio
        

    def compute(self, lista):
        if not isinstance(lista, list):
            raise ExamException("The input must be a list")
        if lista is None:
            raise ExamException("The list provided has value None")
        if len(lista) < 2:
            raise ExamException("The list must be composed of at least 2 elements")
        diff = []
        for i in range(len(lista) - 1):
            if not isinstance(lista[i + 1], (int, float)):
                    raise ExamException("The value in the series is not a number")
            element = lista[i + 1] - lista[i]
            diff.append(element)
        diff[:] = [item / self.ratio for item in diff]
        return diff


diff = Diff(3.7)        