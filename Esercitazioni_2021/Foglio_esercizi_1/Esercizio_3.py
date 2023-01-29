from datetime import datetime 

class CSVFile():

  def __init__(self, name):
    self.name = name

  def __str__(self):
    list = []
    
    my_file = open(self.name, 'r')

    for line in my_file:
      elements = line.split(',')
      if elements[0] == "Date":
        list = elements

    return list

  def get_data(self):
    list = []
    
    my_file = open(self.name, 'r')

    for line in my_file:
      elements = line.split(',')
      if(elements[0] != 'Date'):
        elements[1] = elements[1].replace('\n','')
        list.append(elements)

    return list

  def get_date_vendita(self):
    dates = []

    my_file = open(self.name,"r")
    for line in my_file:
      elements = line.split(",")
      if elements[0] != 'Date':
        try:
          value_t = datetime.strptime(elements[0], '%d-%m-%Y')
          dates.append(value_t)
        except ValueError:
          print("Not a date")
    return dates
        
      

F = CSVFile("shampoo_sales.csv")
file = F.__str__()
print(file)
      