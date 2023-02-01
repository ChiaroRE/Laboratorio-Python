class ExamException(Exception):
        pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        list = []

        try:
          my_file = open(self.name, 'r')
        except FileNotFoundError:
          raise ExamException("Il file {} non è stato trovato".format(self.name))
        except:
          raise ExamException("Il file {} non è leggibile".format(self.name))

        for line in my_file:
            elements = line.split(",")
            if(elements[0] != 'epoch'):
              try:
                  element1 = float(elements[1].replace('\n',''))
              except ValueError:
                continue
              try:
                element0 = int(elements[0])
              except ValueError:
                continue
              if element0 and element1:
                list.append([element0,element1])

        return list

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
            diff.append(max(temp) - min(temp))
            day_end_epoch = day_end_epoch + 86399
            temp = [item[1]]
            

    return diff
  
  

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()

diff = (compute_daily_max_difference(time_series))
print(diff)
print(len(diff))


