class ExamException(Exception):
        pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []

        try:
          my_file = open(self.name, 'r')
        except FileNotFoundError:
          raise ExamException("Il file {} non è stato trovato".format(self.name))
        except Exception:
          raise ExamException("Il file {} non è leggibile".format(self.name))

        if self.name.endswith(".csv") == False:
            raise ExamException("Il file {} non è un file csv".format(self.name))
        else:
            pass

        for line in my_file:
            elements = line.split(",")
            try:
                element1 = float(elements[1].replace('\n',''))
                element0 = int(elements[0])
                lista.append([element0,element1])
            except ValueError or TypeError:
                continue

        if (len(lista) == 0):
            raise ExamException("La lista è vuota")

        for i in range(len(lista) - 1):
            if lista[i][0] >= lista[i + 1][0]:
                Flag_d = False
                j = 0
                while((Flag_d == False) and j != (len(lista) - 1)):
                    if lista[i][0] == lista[j][0] and i != j:
                        Flag_d = True
                    j += 1
                if Flag_d == True:
                    raise ExamException("La serie temporale presenta duplicati")
                else:
                    raise ExamException("La serie temporale non è ordinata")

        return lista

def compute_daily_max_difference(time_series):
    first_element = time_series[0]
    last_element = time_series[-1]
  
    day_start_epoch = first_element[0] - (first_element[0] % 86400)
    day_end_epoch = day_start_epoch + 86399
  
    diff = []
    temp = []
    
    for item in time_series:
        if item[0] <= day_end_epoch:
            temp.append(item[1])
        if item[0] > day_end_epoch or item[0] == last_element[0]:
            var = max(temp) - min(temp)
            if(len(temp) == 1):
                var = None
            diff.append(var)
            day_end_epoch = day_end_epoch + 86399
            temp = [item[1]]
            

    return diff
