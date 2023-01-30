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
                  elements[1] = float(elements[1].replace('\n',''))
              except ValueError:
                continue
              try:
                elements[0] = int(elements[0])
              except ValueError:
                continue
              if elements[0] and elements[1]:
                list.append(elements)

        return list

def compute_daily_max_difference(time_series):
  first_element = time_series[0]
  last_element = time_series[-1]
  
  day_start_epoch = first_element[0] - (first_element[0] % 86400)
  day_end_epoch = day_start_epoch + 86399
  
  day_temp_1 = []
  for item in time_series:
    if item[0] < day_end_epoch and item[0] >= day_start_epoch:
      day_temp_1.append(item[1])
  diff = []
  if len(day_temp_1) <= 1:
    differenza_massima_giorno = None
  else:
    differenza_massima_giorno = max(day_temp_1) - min(day_temp_1)
  diff.append(differenza_massima_giorno)
  
  day_start_epoch = day_end_epoch + 1
  day_end_epoch = day_end_epoch + 86399
  
  while(day_end_epoch < last_element[0]):
    day_temp = []
    for item in time_series:
      if item[0] < day_end_epoch and item[0] >= day_start_epoch:
        day_temp.append(item[1])
    if(len(day_temp) <= 1):
      differenza_massima_giorno = None
    else:
      differenza_massima_giorno = max(day_temp) - min(day_temp)
    diff.append(differenza_massima_giorno)
    day_start_epoch = day_end_epoch + 1
    day_end_epoch = day_end_epoch + 86399

  return diff
  
  

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()

diff = (compute_daily_max_difference(time_series))
print(diff)