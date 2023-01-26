class Model():

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
    raise NotImplementedError('Metodo non implementato')

class FitIncrementModel(Model):
  
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