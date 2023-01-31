class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,window):
        if (type(window) != int):
            raise ExamException("The window inserted is not correct")
        elif(window < 1):
            raise ExamException("The window must be greater or equal than 2")
        self.window = window
            
        

    def compute(self, lista):
        if not isinstance(lista, list):
            raise ExamException("The input must be a list")
        if lista is None:
            raise ExamException("The list provided has value None")
        elif self.window > len(lista):
            raise ExamException("The window is too large for the series")
        if self.window == 1:
            return lista
        res = []
        for i in range(0,len(lista) - (self.window - 1)):
            avg = 0
            for j in range(self.window):
                if not isinstance(lista[i + j], (int, float)):
                    raise ExamException("The value in the series is not a number")
                avg = avg + lista[i + j]
            avg = avg / self.window
            res.append(avg)
        return res

