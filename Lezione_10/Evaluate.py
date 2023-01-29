class Model():

  def __init__(self, finestra):
    self.finestra = finestra
    if finestra < 1 or type(finestra) != int:
      raise Exception("La finestra temporale inserita è incorretta")

  def fit(self,data):
    raise NotImplementedError('Metodo non implementato')

  def predict(self,data):
    raise NotImplementedError('Metodo non implementato')

  def evaluate(self,data,finestra):
    raise NotImplementedError('Metodo non implementato')
   
class IncrementModel(Model):
  
  def __init__(self, finestra):
    super().__init__(finestra)
    
  def predict(self,data):
    prev_value = None
    somma = 0
    for i in range(len(data) - 1):
      somma = somma + (data[i+1] - data[i]) 
    try:
      inc_medio = somma / (len(data) - 1)
    except((len(data) - 1) == 0):
      raise Exception('Non si può fare una predizione da un singolo elemento')
      
    prev_value = data[-1] + inc_medio
    return prev_value

  def evaluate(self,data): 
    prev = []
    for i in range(self.finestra):
      p = self.predict(range(data[-(self.finestra - i)]))
      prev.append(p)
    errori = []
    for i in range(self.finestra - 1):
      e = abs(prev[i] - data[-(self.finestra - i - 1)])
      errori.append(e)
    errore_medio = 0
    for i in range(len(errori) - 1):
      errore_medio = errore_medio + errori[i]
    errore_medio = errore_medio / (len(errori) - 1)

    return errore_medio
    

class FitIncrementModel(Model):

  def __init__(self, finestra):
    super().__init__(finestra)
    
  def fit(self,data):
    somma = 0
    for i in range(len(data) - 1):
      somma = somma + (data[i+1] - data[i]) 
    try:
      inc_medio = somma / (len(data) - 1)
      self.global_avg_increment = inc_medio
    except((len(data) - 1) == 0):
      raise Exception('Non si può fare una predizione da un singolo elemento')
  
  def predict(self,data):
    prev_value = None
    somma = 0
    try:
      for i in range(len(data) - 1):
        somma = somma + (data[i+1] - data[i]) 
      inc_medio_1 = somma / (len(data) - 1)
      inc_medio_tot = (inc_medio_1 + self.global_avg_increment)/2
    except (len(data) < 3):
      raise Exception("Il numero di dati non è abbastanza lungo")
      
    prev_value = data[-1] + inc_medio_tot
    return prev_value

  def evaluate(self,data): 
    prev = []
    for i in range(len(data) - 1):
      p = self.predict(range(data[-(self.finestra - i)]))
      print(p)
      prev.append(p)
    errori = []
    for i in range(len(data) - 1):
      e = abs(prev[i] - data[-(self.finestra - i - 1)])
      print(e)
      errori.append(e)
    errore_medio = 0
    for i in range(len(errori) - 1):
      errore_medio = errore_medio + errori[i]
    errore_medio = int(errore_medio / (len(errori) - 1))

    return errore_medio

data = IncrementModel(3)
evaluation = IncrementModel.evaluate(data,[51,52,53,54,57])
print(evaluation)

class FitIncrementModel(Model):

  def __init__(self, finestra):
    super().__init__(finestra)
    
  def fit(self,data):
    somma = 0
    for i in range(len(data) - 1):
      somma = somma + (data[i+1] - data[i]) 
    try:
      inc_medio = somma / (len(data) - 1)
      self.global_avg_increment = inc_medio
    except((len(data) - 1) == 0):
      raise Exception('Non si può fare una predizione da un singolo elemento')
  
  def predict(self,data):
    prev_value = None
    somma = 0
    try:
      for i in range(len(data) - 1):
        somma = somma + (data[i+1] - data[i]) 
      inc_medio_1 = somma / (len(data) - 1)
      inc_medio_tot = (inc_medio_1 + self.global_avg_increment)/2
    except (len(data) < 3):
      raise Exception("Il numero di dati non è abbastanza lungo")
      
    prev_value = data[-1] + inc_medio_tot
    return prev_value

  def evaluate(self,data): 
    prev = []
    for i in range(len(data) - 1):
      p = self.predict(range(data[-(self.finestra - i)]))
      print(p)
      prev.append(p)
    errori = []
    for i in range(len(data) - 1):
      e = abs(prev[i] - data[-(self.finestra - i - 1)])
      print(e)
      errori.append(e)
    errore_medio = 0
    for i in range(len(errori) - 1):
      errore_medio = errore_medio + errori[i]
    errore_medio = int(errore_medio / (len(errori) - 1))

    return errore_medio

#lista = [67,72,72,67,72]
#mod = IncrementModel(5)
err = mod.evaluate(lista)
print(err)

my_file = open("shampoo_sales_(copy).csv", "r")
values = []
for line in my_file:
  elements = line.split(',')

  if elements[0] != 'Date':
    try:
      value_t = float(elements[1])
      values.append(value_t)
    except ValueError:
      print("Not a float")
      
fit = values[0:24]
eval = values[24:36]
mod1 = IncrementModel(12)
err1 = mod1.evaluate(values)
print(err1)