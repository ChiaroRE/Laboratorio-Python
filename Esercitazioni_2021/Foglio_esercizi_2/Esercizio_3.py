import random

class CSVFile():

  def __init__(self, name):
    if isinstance(name,str) == False:
      raise TypeError('La variabile non è una stringa')
    self.name = name

  def get_data(self, start = None, end = None):
    list = []
    
    try:
      my_file = open(self.name, 'r')
      lines = my_file.readlines()
      
    except FileNotFoundError:
      print('Errore : file inesistente')

    if isinstance(start,str) != False:
      try:
        start = int(start)
      except ValueError:
        raise ValueError('Il parametro start non è un numero')

    if isinstance(end,str) != False:
      try:
        end = int(end)
      except ValueError:
        raise ValueError('parametro end non è un numero')
      
    if start and start > len(lines):
      raise ValueError("start è maggiore delle righe")
    if end and end > len(lines):
      raise ValueError("end è maggiore delle righe")

    if start == None and end == None:
      for line in lines:
        elements = line.strip().split(',')
        if(elements[0] != 'Date'):
          elements[1] = float(elements[1].replace('\n',''))
          list.append(elements)
          
    elif start == None and end != None:
      for i in range(end):
        elements = lines[i].strip().split(',')
        if(elements[0] != 'Date'):
          elements[1] = float(elements[1].replace('\n',''))
          list.append(elements)
          
    elif start != None and end == None:
      if start < 1:
        raise ValueError('Il parametro start non è corretto')
      for i in range(start - 1,len(lines)):
        elements = lines[i].strip().split(',')
        if(elements[0] != 'Date'):
          elements[1] = float(elements[1].replace('\n',''))
          list.append(elements)   
    else:
      if start <= 0 or start > end:
        raise ValueError('I parametri non sono corretti')
      else: 
        for i in range(start-1,end):
          elements = lines[i].strip().split(',')
          if(elements[0] != 'Date'):
            elements[1] = float(elements[1].replace('\n',''))
            list.append(elements)
        
      
    return list

class Test():
    
    def __init__(self):
        self.file_test = CSVFile("shampoo_sales.csv")
    
    def test_sum(self):
        size = len(self.file_test.get_data()) + 1
        F1 = self.file_test.get_data()
        F2 = self.file_test.get_data(1,size)
        SumF1 = 0
        for item in F1:
            SumF1 = SumF1 + item[1]
        SumF2 = 0
        for item in F2:
            SumF2 = SumF2 + item[1]
        if SumF1 != SumF2:
            raise Exception("The sum of the function with borders and without borders is different, {} != {}".format(SumF1,SumF2))
        else:
            print("No errors for test_sum")

    def test_rand(self):
        size = len(self.file_test.get_data()) + 1
        int = random.randint(1,size)
        F1 = self.file_test.get_data()
        F2 = self.file_test.get_data(1,int)
        SumF1 = 0
        for item in F1:
            SumF1 = SumF1 + item[1]
        SumF2 = 0
        for item in F2:
            SumF2 = SumF2 + item[1]
        if SumF1 < SumF2:
            raise Exception("The sum of the function with borders is larger than without borders, {} > {}".format(SumF1,SumF2))
        else:
            print("No errors for test_rand")
        
        
        
test = Test()
test.test_sum()
test.test_rand()